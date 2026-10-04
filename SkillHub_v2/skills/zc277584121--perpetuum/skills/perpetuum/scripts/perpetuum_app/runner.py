"""Background scheduler and top-level interactive session lifecycle."""

from __future__ import annotations

import argparse
import os
import shutil
import signal
import sys
import time
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from . import scheduler, sessions, storage
from .server import RuntimeServer


TOP_SESSION_MISSING_GRACE = timedelta(minutes=5)
CHAIN_SETTLED_GRACE = timedelta(minutes=5)
STABLE_PROJECT_STATUSES = {"idle", "waiting_human", "control_blocked"}


class Runner:
    def __init__(self, home: Path) -> None:
        self.home = home
        self.skill_root = Path(__file__).resolve().parents[2]
        self.state = storage.read_json(
            storage.runner_state_path(home),
            storage.default_runner_state(),
        )
        if not isinstance(self.state, dict):
            self.state = storage.default_runner_state()
        self.state.setdefault("active_projects", {})
        self.state.setdefault("last_schedule_slots", {})
        self.state.setdefault("schedule_errors", {})
        self.force_stop = False

    def save_state(self) -> None:
        storage.write_json(storage.runner_state_path(self.home), self.state)

    def event(self, event: str, **fields: Any) -> None:
        storage.append_event(storage.runner_events_path(self.home), event, **fields)

    def current_time(self) -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def format_time(value: datetime) -> str:
        return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")

    @staticmethod
    def parse_time(value: Any) -> Optional[datetime]:
        if not isinstance(value, str) or not value:
            return None
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
        if parsed.tzinfo is None:
            return None
        return parsed.astimezone(timezone.utc)

    def safe_run_dir(self, run_dir: Path) -> bool:
        root = (storage.runner_dir(self.home) / "runs").resolve()
        try:
            relative = run_dir.resolve().relative_to(root)
        except (OSError, ValueError):
            return False
        return bool(relative.parts)

    def cleanup_run_dir(self, run_dir: Path) -> None:
        if self.safe_run_dir(run_dir):
            shutil.rmtree(run_dir, ignore_errors=True)
            return
        self.event("unsafe_run_dir_ignored", run_dir=str(run_dir))

    def project_payload(self, project_id: str) -> Optional[Dict[str, Any]]:
        project = storage.load_project(self.home, project_id)
        if not project:
            self.write_control_escalation(
                project_id,
                "Runner 找不到项目配置",
                "项目已经注册，但 project.yaml 缺失或无法解析。",
                "请检查项目 Harness 是否被移动或损坏。",
            )
            return None
        project_path = Path(str(project.get("path", ""))).expanduser()
        if not project_path.is_dir():
            self.write_control_escalation(
                project_id,
                "Runner 无法访问项目目录",
                f"project.yaml 指向的目录不存在或不可访问：{project_path}",
                "请恢复目录或修正 project.yaml 后再使用“立即运行”验证。",
            )
            return None
        raw_agent = project.get("agent", {})
        agent = raw_agent if isinstance(raw_agent, dict) else {}
        kind = str(agent.get("kind", "codex"))
        if kind not in {"codex", "claude"}:
            self.write_control_escalation(
                project_id,
                "Runner 无法识别 Agent 类型",
                f"project.yaml 中的 Agent 类型无效：{kind}",
                "请把 Agent 类型修正为 codex 或 claude。",
            )
            return None
        return {
            "id": project_id,
            "name": project.get("name", project_id),
            "path": str(project_path.resolve()),
            "harness": str(storage.project_dir(self.home, project_id)),
            "agent": {"kind": kind},
        }

    def create_run(
        self,
        role: str,
        carrier_session: str,
        payload: Dict[str, Any],
    ) -> Tuple[Path, Path, Path, str]:
        run_id = (
            f"{role}-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-"
            f"{os.getpid()}-{time.monotonic_ns() % 1_000_000:06d}"
        )
        run_dir = storage.runner_dir(self.home) / "runs" / run_id
        run_dir.mkdir(parents=True, exist_ok=False)
        dispatch_path = run_dir / "dispatch.json"
        receipt_path = run_dir / "receipt.json"
        playbooks = self.skill_root / "references" / "playbooks"
        references = {
            "architecture": str(self.skill_root / "references" / "architecture.md"),
            "runtime": str(self.skill_root / "references" / "runtime.md"),
            "human_communication": str(
                self.skill_root / "references" / "human-communication.md"
            ),
        }
        references["project_supervisor"] = str(
            playbooks / "project-supervisor.md"
        )
        references["story_supervisor"] = str(
            playbooks / "story-supervisor.md"
        )
        dispatch = {
            "version": 1,
            "role": role,
            "run_id": run_id,
            "created_at": storage.utc_now(),
            "perpetuum_home": str(self.home),
            "runner_state": str(storage.runner_state_path(self.home)),
            "carrier_session": carrier_session,
            "references": references,
            "receipt_path": str(receipt_path),
            **payload,
        }
        storage.write_json(dispatch_path, dispatch)
        return run_dir, dispatch_path, receipt_path, run_id

    def build_project_prompt(
        self,
        dispatch_path: Path,
        receipt_path: Path,
        carrier_session: str,
        project: Dict[str, Any],
        trigger: Dict[str, Any],
    ) -> str:
        playbook_path = (
            self.skill_root
            / "references"
            / "playbooks"
            / "project-supervisor.md"
        )
        reason = (
            f"cron `{trigger.get('matched_cron')}` 匹配"
            if trigger.get("reason") == "cron"
            else "人类请求立即运行"
        )
        return f"""你是项目“{project['name']}”本次激活的 Project Supervisor。

项目目录：{project['path']}
Harness：{project['harness']}
本次触发：{reason}
触发时间：{trigger.get('triggered_at')}
本次 dispatch：{dispatch_path}
角色 Playbook：{playbook_path}
完成回执：{receipt_path}
当前承载 session：{carrier_session}

这是一次新的独立激活。先完整读取 dispatch、角色 Playbook 和项目当前状态，再决定本轮是否值得推进一张 Story。不要机械重复上一次运行的动作。

工作时遵守以下边界：
- 当前承载 session 由 Runner 创建和回收，不是你创建的直属子 session；不要关闭、接管或向它发送消息。
- `team.md` 是本项目的队伍与角色编排契约。Executor 必须启用；Validator 和 Explorer 只在契约启用并满足触发条件时创建，不得擅自补齐固定角色链。
- 需要推进 Story 时，通过当前安装的 cc-use Skill 创建唯一的 Story Supervisor；不要在这里硬编码或猜测 cc-use 的具体命令和参数。
- 同一项目本轮最多推进一张 Story。没有可运行 Story 时，只在 `team.md` 启用 Explorer 且配置了该触发条件时调用它整理看板；否则正常返回 Idle。
- 只管理本次由你明确创建并保存了精确名称的直属子 session；全局 session 列表和项目状态只能用于观察，不能证明所有权。
- 创建直属角色后立即持久化 `start` 返回的精确名称；关闭时先保存 `finish` 的结构化结果。最终回执包含逐条的 direct_sessions 生命周期证据，缺失时如实保留管控缺口。
- 根据 Playbook、Harness 和实际结果组织下级 Prompt。不要因为时间经过、session 仍存活或屏幕暂时没有变化，就发送固定的“继续”Prompt。
- 不使用非交互式 Agent 模式代替 TUI。无人值守运行期间，不自动更新 Codex、Claude Code、模型或认证配置。
- 无论成功、Idle、等待还是无法继续，都先关闭并复核自己创建的全部直属子 session，再更新项目状态。
- 最后把一个 JSON 对象原子写入 {receipt_path}。至少包含 status、summary、project_id、finished_at；先写同目录临时文件，再重命名。
- 写完回执后等待 Runner 回收当前 session，不要自行启动长期等待或定时 Prompt 循环。
"""

    def launch_project(
        self,
        project_id: str,
        trigger: Dict[str, Any],
        config: Dict[str, Any],
    ) -> Optional[Dict[str, Any]]:
        try:
            project = self.project_payload(project_id)
        except ValueError as exc:
            self.write_control_escalation(
                project_id,
                "Runner 无法读取项目计划",
                str(exc),
                "请修正 schedule.yaml 后再使用“立即运行”验证。",
            )
            return None
        if project is None:
            return None
        carrier_session = sessions.session_name("project", project_id)
        run_dir, dispatch_path, receipt_path, run_id = self.create_run(
            "project",
            carrier_session,
            {"project": project, "trigger": trigger},
        )
        kind = str(project["agent"].get("kind", "codex"))
        startup_seconds = int(
            config.get("service", {}).get("agent_startup_seconds", 8)
        )
        prompt = self.build_project_prompt(
            dispatch_path,
            receipt_path,
            carrier_session,
            project,
            trigger,
        )
        try:
            command = sessions.agent_command(kind)
            session = sessions.launch_session(
                role="project",
                command=command,
                cwd=Path(project["path"]),
                prompt=prompt,
                startup_seconds=startup_seconds,
                kind=kind,
                name=carrier_session,
            )
        except Exception as exc:
            self.cleanup_run_dir(run_dir)
            self.write_control_escalation(
                project_id,
                "无法启动 Project Supervisor session",
                str(exc),
                "请检查 tmux、Agent TUI、环境变量和认证，再使用“立即运行”验证。",
            )
            self.state["last_error"] = str(exc)
            self.event(
                "project_session_launch_failed",
                project_id=project_id,
                error=str(exc),
            )
            return None
        active = {
            "role": "project",
            "run_id": run_id,
            "session": session,
            "project_id": project_id,
            "dispatch_path": str(dispatch_path),
            "receipt_path": str(receipt_path),
            "run_dir": str(run_dir),
            "trigger": trigger,
            "started_at": storage.utc_now(),
        }
        self.event(
            "project_session_started",
            project_id=project_id,
            run_id=run_id,
            session=session,
            trigger=trigger,
        )
        return active

    def reconcile_active(
        self,
        active: Dict[str, Any],
        project_ids: List[str],
    ) -> bool:
        session = str(active.get("session", ""))
        receipt_path = Path(str(active.get("receipt_path", "")))
        run_dir = Path(str(active.get("run_dir", "")))
        role = str(active.get("role", "unknown"))
        owned_session = sessions.is_owned_top_session(session, role)
        valid_receipt = (
            self.safe_run_dir(run_dir)
            and receipt_path.name == "receipt.json"
            and receipt_path.parent.resolve() == run_dir.resolve()
        )
        if valid_receipt and receipt_path.is_file():
            receipt = storage.read_json(receipt_path, {})
            if owned_session and sessions.session_exists(session):
                sessions.kill_session(session)
            self.event(
                "top_session_completed",
                role=role,
                run_id=active.get("run_id"),
                session=session,
                project_ids=project_ids,
                receipt=receipt,
            )
            self.cleanup_run_dir(run_dir)
            return True

        if not valid_receipt or not owned_session:
            for project_id in project_ids:
                self.write_control_escalation(
                    project_id,
                    f"{role} 运行元数据无效",
                    (
                        f"Runner 无法安全核验 tmux session {session} 与回执路径"
                        f" {receipt_path}。"
                    ),
                    "请检查 runner/events.log 和 runner/state.json，确认运行记录没有损坏。",
                )
            self.event(
                "top_session_lost",
                role=role,
                run_id=active.get("run_id"),
                session=session,
                project_ids=project_ids,
                reason="invalid_metadata",
            )
            self.cleanup_run_dir(run_dir)
            return True

        if sessions.session_exists(session):
            recovered = any(
                field in active
                for field in (
                    "carrier_missing_since",
                    "top_session_orphaned_at",
                    "chain_settled_since",
                )
            )
            active.pop("carrier_missing_since", None)
            active.pop("top_session_orphaned_at", None)
            active.pop("chain_settled_since", None)
            if recovered:
                self.event(
                    "top_session_recovered",
                    role=role,
                    run_id=active.get("run_id"),
                    session=session,
                    project_ids=project_ids,
                )
            return False

        now = self.current_time()
        missing_since = self.parse_time(active.get("carrier_missing_since"))
        if missing_since is None:
            active["carrier_missing_since"] = self.format_time(now)
            active.pop("top_session_orphaned_at", None)
            active.pop("chain_settled_since", None)
            self.event(
                "top_session_missing",
                role=role,
                run_id=active.get("run_id"),
                session=session,
                project_ids=project_ids,
            )
            return False

        if now < missing_since + TOP_SESSION_MISSING_GRACE:
            return False

        if "top_session_orphaned_at" not in active:
            active["top_session_orphaned_at"] = self.format_time(now)
            self.event(
                "top_session_orphaned",
                role=role,
                run_id=active.get("run_id"),
                session=session,
                project_ids=project_ids,
            )

        project_states = [
            storage.load_project_state(self.home, project_id)
            for project_id in project_ids
        ]
        chain_settled = bool(project_states) and all(
            self.project_chain_is_settled(project_state, missing_since)
            for project_state in project_states
        )
        if not chain_settled:
            active.pop("chain_settled_since", None)
            return False

        settled_since = self.parse_time(active.get("chain_settled_since"))
        if settled_since is None:
            active["chain_settled_since"] = self.format_time(now)
            return False
        if now < settled_since + CHAIN_SETTLED_GRACE:
            return False

        for project_id in project_ids:
            self.write_control_escalation(
                project_id,
                f"{role} session 消失且稳定链路未写入完成回执",
                (
                    f"Runner 检查到 tmux session {session} 已不存在；项目运行状态在"
                    " carrier 消失后更新到稳定状态并持续五分钟，但仍没有找到回执文件"
                    f" {receipt_path}。运行目录将保留作为证据。"
                ),
                (
                    "请查看 runner/events.log、保留的运行目录和项目 runtime/events.log，"
                    "确认回执为何缺失以及是否存在遗留的下层 session。"
                ),
            )
        self.event(
            "top_session_lost",
            role=role,
            run_id=active.get("run_id"),
            session=session,
            project_ids=project_ids,
            reason="chain_settled_without_receipt",
            run_dir=str(run_dir),
        )
        return True

    def project_chain_is_settled(
        self,
        project_state: Dict[str, Any],
        missing_since: datetime,
    ) -> bool:
        last_activity_at = self.parse_time(project_state.get("last_activity_at"))
        active_sessions = project_state.get("active_sessions")
        return (
            last_activity_at is not None
            and last_activity_at > missing_since
            and project_state.get("current_story") is None
            and isinstance(active_sessions, list)
            and not active_sessions
            and project_state.get("status") in STABLE_PROJECT_STATUSES
        )

    def reconcile_projects(self) -> None:
        active_projects = self.state.setdefault("active_projects", {})
        if not isinstance(active_projects, dict):
            active_projects = {}
            self.state["active_projects"] = active_projects
        for project_id, active in list(active_projects.items()):
            if not isinstance(active, dict) or self.reconcile_active(
                active,
                [project_id],
            ):
                active_projects.pop(project_id, None)

    def write_control_escalation(
        self,
        project_id: str,
        title: str,
        detail: str,
        action: str,
    ) -> None:
        harness = storage.project_dir(self.home, project_id)
        if not harness.is_dir():
            self.event(
                "unattached_escalation",
                project_id=project_id,
                title=title,
                detail=detail,
            )
            return
        block = (
            f"\n\n### {title} · {storage.utc_now()}\n\n"
            f"**发生了什么**\n\n{detail}\n\n"
            "**影响**\n\n本次自动工作链路没有获得可信完成结果，"
            "项目不会把这次运行计为已完成 Story。\n\n"
            "**已尝试的恢复**\n\nRunner 已检查完成回执和 Project Supervisor tmux session，"
            "并停止继续假设本次运行成功。\n\n"
            "**为什么不能自动处理**\n\n继续重试可能重复消耗额度、覆盖现场或制造并行 Story，"
            "需要先确认底层原因。\n\n"
            f"**人类需要做什么**\n\n{action}\n\n"
            "**恢复验证**\n\n处理后触发一次项目运行，确认 Project 与 Story 链路"
            "能够写入可信完成回执。\n\n"
            f"**原始状态**\n\n- Runner 日志：`{storage.runner_events_path(self.home)}`\n"
            f"- 项目运行日志：`{harness / 'runtime' / 'events.log'}`\n"
        )
        path = harness / "escalations.md"
        descriptor = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
        try:
            os.write(descriptor, block.encode("utf-8"))
        finally:
            os.close(descriptor)
        project_state = storage.load_project_state(self.home, project_id)
        project_state.update(
            {
                "status": "control_blocked",
                "last_activity_at": storage.utc_now(),
                "last_result": title,
            }
        )
        storage.write_json(harness / "runtime" / "state.json", project_state)
        storage.append_event(
            harness / "runtime" / "events.log",
            "control_escalation",
            title=title,
        )

    def read_project_schedule(self, project_id: str) -> Optional[Dict[str, Any]]:
        errors = self.state.setdefault("schedule_errors", {})
        try:
            schedule = storage.load_project_schedule(self.home, project_id)
        except ValueError as exc:
            message = str(exc)
            if errors.get(project_id) != message:
                self.write_control_escalation(
                    project_id,
                    "项目运行计划无效",
                    message,
                    "请修正 schedule.yaml 中的时区和标准五字段 cron 表达式。",
                )
                errors[project_id] = message
            return None
        errors.pop(project_id, None)
        return schedule

    def tick(self) -> None:
        config = storage.ensure_home(self.home)
        now = datetime.now(timezone.utc)
        self.state["last_tick_at"] = storage.utc_now()
        self.state["next_schedule_check_at"] = scheduler.next_schedule_check(now)

        self.reconcile_projects()

        service = config.get("service", {})
        if service.get("stop_requested", False) or service.get(
            "restart_requested", False
        ):
            self.state["service"]["status"] = "draining"
            self.save_state()
            return

        active_projects = self.state.setdefault("active_projects", {})
        last_slots = self.state.setdefault("last_schedule_slots", {})
        for project_id in storage.list_project_ids(self.home):
            schedule = self.read_project_schedule(project_id)
            if schedule is None:
                continue
            trigger = scheduler.project_trigger(
                schedule,
                last_slots.get(project_id),
                now,
            )
            if trigger is None:
                continue
            if trigger.get("cron_minute"):
                last_slots[project_id] = trigger["cron_minute"]
            if project_id in active_projects:
                if trigger.get("reason") == "manual":
                    storage.consume_project_force_flags(self.home, [project_id])
                self.event(
                    "project_activation_skipped",
                    project_id=project_id,
                    reason="already_active",
                    trigger=trigger,
                )
                continue
            active = self.launch_project(project_id, trigger, config)
            if trigger.get("reason") == "manual":
                storage.consume_project_force_flags(self.home, [project_id])
            if active is not None:
                active_projects[project_id] = active

        self.state["last_error"] = None
        self.save_state()

    def should_exit(self) -> Optional[str]:
        config = storage.ensure_home(self.home)
        service = config.get("service", {})
        if self.force_stop:
            return "stop"
        if self.state.get("active_projects"):
            return None
        if service.get("restart_requested", False):
            return "restart"
        if service.get("stop_requested", False):
            return "stop"
        return None

    def force_cleanup(self) -> None:
        active_projects = self.state.get("active_projects", {})
        if isinstance(active_projects, dict):
            for project_id, active in list(active_projects.items()):
                if not isinstance(active, dict):
                    continue
                session = str(active.get("session", ""))
                if sessions.is_owned_top_session(
                    session, "project"
                ) and sessions.session_exists(session):
                    sessions.kill_session(session)
                self.write_control_escalation(
                    project_id,
                    "Perpetuum 服务被强制停止",
                    f"Project Supervisor session {session} 在未完成回执时被终止。",
                    "确认没有遗留的子 session 或半完成业务变更，再重新启动服务并手动触发项目验证。",
                )
            self.state["active_projects"] = {}


def reset_service_request(home: Path, key: str) -> None:
    config = storage.ensure_home(home)
    service = config.setdefault("service", {})
    service[key] = False
    storage.write_json(storage.activation_path(home), config)


def run_daemon(home: Path) -> int:
    config = storage.ensure_home(home)
    runner = Runner(home)
    service = config.get("service", {})
    host = str(service.get("host", "127.0.0.1"))
    port = int(service.get("port", 8765))
    heartbeat = max(1, int(service.get("heartbeat_seconds", 5)))

    def handle_signal(signum: int, frame: Any) -> None:
        del signum, frame
        runner.force_stop = True

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    try:
        server = RuntimeServer(home, host, port)
        server.start()
    except Exception as exc:
        runner.state["service"] = {
            "status": "stopped",
            "pid": None,
            "started_at": None,
            "stopped_at": storage.utc_now(),
            "url": f"http://{host}:{port}",
        }
        runner.state["last_error"] = str(exc)
        runner.save_state()
        runner.event("service_start_failed", error=str(exc), host=host, port=port)
        return 1

    runner.state["service"] = {
        "status": "running",
        "pid": os.getpid(),
        "started_at": storage.utc_now(),
        "stopped_at": None,
        "url": f"http://{host}:{port}",
    }
    runner.save_state()
    runner.event("service_started", pid=os.getpid(), host=host, port=port)
    exit_mode = "stop"
    try:
        while True:
            try:
                runner.tick()
            except Exception as exc:
                runner.state["last_error"] = str(exc)
                runner.save_state()
                runner.event(
                    "runner_tick_failed",
                    error=str(exc),
                    traceback=traceback.format_exc(),
                )
            exit_mode = runner.should_exit() or ""
            if exit_mode:
                break
            time.sleep(heartbeat)
    finally:
        server.stop()
        if runner.force_stop:
            runner.force_cleanup()
        runner.state["service"].update(
            {
                "status": "stopped",
                "pid": None,
                "stopped_at": storage.utc_now(),
            }
        )
        runner.save_state()
        runner.event("service_stopped", mode=exit_mode)

    if exit_mode == "restart" and not runner.force_stop:
        reset_service_request(home, "restart_requested")
        reset_service_request(home, "stop_requested")
        os.execv(
            sys.executable,
            [
                sys.executable,
                "-m",
                "perpetuum_app.runner",
                "--home",
                str(home),
            ],
        )
    reset_service_request(home, "stop_requested")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Perpetuum background runner")
    parser.add_argument("--home", type=Path)
    args = parser.parse_args()
    raise SystemExit(run_daemon(storage.runtime_home(args.home)))


if __name__ == "__main__":
    main()
