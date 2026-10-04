"""Command-line entry point for Perpetuum."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.error import URLError
from urllib.request import Request, urlopen

from . import storage
from .server import global_status, process_alive


def load_state(home: Path) -> Dict[str, Any]:
    value = storage.read_json(
        storage.runner_state_path(home),
        storage.default_runner_state(),
    )
    return value if isinstance(value, dict) else storage.default_runner_state()


def service_pid(home: Path) -> Optional[int]:
    pid = load_state(home).get("service", {}).get("pid")
    return pid if isinstance(pid, int) and process_alive(pid) else None


def update_service_config(home: Path, **changes: Any) -> Dict[str, Any]:
    config = storage.ensure_home(home)
    service = config.setdefault("service", {})
    service.update(changes)
    storage.write_json(storage.activation_path(home), config)
    return config


def connect_host(host: str) -> str:
    if host in {"", "0.0.0.0"}:
        return "127.0.0.1"
    if host == "::":
        return "::1"
    return host


def service_url(host: str, port: int) -> str:
    target = connect_host(host)
    display = f"[{target}]" if ":" in target and not target.startswith("[") else target
    return f"http://{display}:{port}"


def probe_perpetuum(host: str, port: int) -> Optional[Dict[str, Any]]:
    request = Request(
        f"{service_url(host, port)}/api/status",
        headers={"Accept": "application/json"},
    )
    try:
        with urlopen(request, timeout=0.75) as response:
            server = response.headers.get("Server", "")
            payload = json.loads(response.read().decode("utf-8"))
    except (OSError, URLError, ValueError):
        return None
    if not server.startswith("Perpetuum/") or not isinstance(payload, dict):
        return None
    if "runner" not in payload or "projects" not in payload:
        return None
    return payload


def port_in_use(host: str, port: int) -> bool:
    try:
        with socket.create_connection((connect_host(host), port), timeout=0.5):
            return True
    except OSError:
        return False


def start_service(home: Path, host: Optional[str], port: Optional[int]) -> int:
    config = storage.ensure_home(home)
    existing = service_pid(home)
    if existing:
        state = load_state(home)
        url = state.get("service", {}).get("url", "")
        print(f"Perpetuum 已在运行，PID {existing}，前端：{url}")
        return 0

    configured_service = config.get("service", {})
    target_host = host or str(configured_service.get("host", "127.0.0.1"))
    target_port = port if port is not None else int(configured_service.get("port", 8765))
    url = service_url(target_host, target_port)
    running = probe_perpetuum(target_host, target_port)
    if running is not None:
        running_home = running.get("home")
        try:
            running_home_path = (
                Path(str(running_home)).expanduser().resolve()
                if running_home
                else None
            )
        except (OSError, RuntimeError):
            running_home_path = None
        requested_home = home.resolve()
        if running_home_path == requested_home:
            print(f"配置地址已有 Perpetuum 前端，直接复用：{url}")
            return 0
        print(
            f"配置地址已有不同运行时的 Perpetuum：{url}。"
            f"当前请求：{requested_home}；已有运行时：{running_home or '无法确认'}。"
            "不会复用该服务或改用其他端口。",
            file=sys.stderr,
        )
        return 1
    if port_in_use(target_host, target_port):
        print(
            f"端口已被其他服务占用：{target_host}:{target_port}。"
            "不会自动重启该服务或改用其他端口，请先确认冲突。",
            file=sys.stderr,
        )
        return 1

    changes: Dict[str, Any] = {
        "stop_requested": False,
        "restart_requested": False,
    }
    if host:
        changes["host"] = host
    if port is not None:
        changes["port"] = port
    config = update_service_config(home, **changes)

    scripts_dir = Path(__file__).resolve().parents[1]
    environment = os.environ.copy()
    current_python_path = environment.get("PYTHONPATH")
    environment["PYTHONPATH"] = (
        f"{scripts_dir}:{current_python_path}"
        if current_python_path
        else str(scripts_dir)
    )
    log_path = storage.runner_events_path(home)
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "perpetuum_app.runner",
            "--home",
            str(home),
        ],
        cwd=str(scripts_dir),
        env=environment,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
        close_fds=True,
    )

    deadline = time.time() + 8
    while time.time() < deadline:
        pid = service_pid(home)
        if pid:
            service = config.get("service", {})
            print(
                f"Perpetuum 已启动，PID {pid}，前端："
                f"http://{service.get('host', '127.0.0.1')}:{service.get('port', 8765)}"
            )
            return 0
        if process.poll() is not None:
            break
        time.sleep(0.2)
    print(f"Perpetuum 启动失败，请检查 {log_path}", file=sys.stderr)
    return 1


def stop_service(home: Path, force: bool) -> int:
    pid = service_pid(home)
    if not pid:
        print("Perpetuum 当前没有运行。")
        return 0
    if force:
        os.kill(pid, signal.SIGTERM)
        print("已请求强制停止；未完成的顶层 session 会被终止并记录管控异常。")
        return 0

    update_service_config(home, stop_requested=True, restart_requested=False)
    deadline = time.time() + 8
    while time.time() < deadline:
        if not service_pid(home):
            print("Perpetuum 已停止。")
            return 0
        time.sleep(0.25)
    state = load_state(home)
    active_projects = state.get("active_projects", {})
    if active_projects:
        count = len(active_projects) if isinstance(active_projects, dict) else 0
        print(
            "Perpetuum 正在等待当前顶层工作完成，之后会自动停止。"
            f" 当前活跃链路：{count}"
        )
    else:
        print("已提交停止请求，服务将在下一次心跳退出。")
    return 0


def restart_service(home: Path, host: Optional[str], port: Optional[int]) -> int:
    pid = service_pid(home)
    if not pid:
        return start_service(home, host, port)
    changes: Dict[str, Any] = {
        "restart_requested": True,
        "stop_requested": False,
    }
    if host:
        changes["host"] = host
    if port is not None:
        changes["port"] = port
    update_service_config(home, **changes)
    state = load_state(home)
    active_projects = state.get("active_projects", {})
    if active_projects:
        count = len(active_projects) if isinstance(active_projects, dict) else 0
        print(
            "已请求重启。服务会等待当前顶层工作完成后原地重启；"
            f"当前活跃链路：{count}"
        )
    else:
        print("已请求重启，服务将在下一次心跳原地重启。")
    return 0


def print_status(home: Path, as_json: bool) -> int:
    status = global_status(home)
    if as_json:
        print(json.dumps(status, ensure_ascii=False, indent=2))
        return 0
    service = status["runner"].get("service", {})
    alive = service.get("alive", False)
    print(f"服务：{'运行中' if alive else '已停止'}")
    if alive:
        print(f"PID：{service.get('pid')}")
        print(f"前端：{service.get('url')}")
    active_projects = status["runner"].get("active_projects", {})
    print(f"Project Supervisor：{len(active_projects)} 个活跃")
    print(f"项目数：{len(status['projects'])}")
    for project in status["projects"]:
        pause = "（已暂停）" if project.get("paused") else ""
        print(
            f"- {project['id']}: {project['name']} · "
            f"{project.get('status', 'unknown')}{pause}"
        )
    if status["runner"].get("last_error"):
        print(f"最近错误：{status['runner']['last_error']}")
    return 0


def project_add(args: argparse.Namespace, home: Path) -> int:
    try:
        project_id = storage.register_project(
            home=home,
            path=args.path,
            name=args.name,
            project_id=args.id,
            agent=args.agent,
            crons=args.cron,
            timezone_name=args.timezone,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(f"项目已注册：{project_id}")
    print(f"Harness：{storage.project_dir(home, project_id)}")
    return 0


def project_list(home: Path, as_json: bool) -> int:
    projects = [
        {
            "project": storage.load_project(home, project_id),
            "schedule": storage.load_project_schedule(home, project_id),
            "runtime": storage.load_project_state(home, project_id),
        }
        for project_id in storage.list_project_ids(home)
    ]
    if as_json:
        print(json.dumps(projects, ensure_ascii=False, indent=2))
        return 0
    if not projects:
        print("尚未注册项目。")
        return 0
    for item in projects:
        project = item["project"] or {}
        schedule = item["schedule"]
        state = item["runtime"]
        paused = "，已暂停" if schedule.get("paused") else ""
        print(
            f"{project.get('id')}: {project.get('name')} · "
            f"{state.get('status', 'unknown')}{paused}\n"
            f"  {project.get('path')}\n"
            f"  时区：{schedule.get('timezone', 'unknown')}\n"
            f"  Cron：{', '.join(schedule.get('cron', []))}"
        )
    return 0


def project_control(home: Path, project_id: str, action: str) -> int:
    try:
        storage.update_project_control(home, project_id, action)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    labels = {"pause": "暂停", "resume": "恢复", "run": "立即运行"}
    print(f"已提交项目{labels[action]}请求：{project_id}")
    return 0


def project_schedule(
    home: Path,
    project_id: str,
    crons: Any,
    timezone_name: Optional[str],
) -> int:
    try:
        storage.set_project_schedule(
            home,
            project_id,
            list(crons),
            timezone_name,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    schedule = storage.load_project_schedule(home, project_id)
    print(
        f"已更新运行计划：{project_id} · {schedule['timezone']} · "
        f"{', '.join(schedule['cron'])}"
    )
    return 0


def story_list(home: Path, project_id: str, as_json: bool) -> int:
    try:
        stories = storage.list_stories(home, project_id)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if as_json:
        print(json.dumps(stories, ensure_ascii=False, indent=2))
        return 0
    if not stories:
        print("尚未建立 Story。")
        return 0
    for story in stories:
        labels = ", ".join(story.get("labels", [])) or "无标签"
        print(
            f"{story['id']}: [{story['priority']}] {story['title']} · "
            f"{story['status']}\n  {story['summary']}\n  标签：{labels}"
        )
    return 0


def story_show(home: Path, project_id: str, story_id: str, as_json: bool) -> int:
    try:
        story = storage.load_story(home, project_id, story_id)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if as_json:
        print(json.dumps(story, ensure_ascii=False, indent=2))
    else:
        print(Path(story["path"]).read_text(encoding="utf-8"), end="")
    return 0


def story_create(args: argparse.Namespace, home: Path) -> int:
    body = None
    if args.body_file:
        try:
            body = args.body_file.read_text(encoding="utf-8")
        except OSError as exc:
            print(str(exc), file=sys.stderr)
            return 2
    try:
        story = storage.create_story(
            home,
            args.project_id,
            args.title,
            args.summary,
            story_id=args.id,
            status=args.status,
            priority=args.priority,
            labels=args.label,
            body=body,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    metadata = story["metadata"]
    print(f"Story 已创建：{metadata['id']} · {metadata['title']}")
    print(f"文件：{story['path']}")
    return 0


def story_update(args: argparse.Namespace, home: Path) -> int:
    changes = {}
    for field in ("title", "summary", "status", "priority"):
        value = getattr(args, field)
        if value is not None:
            changes[field] = value
    if args.label is not None:
        changes["labels"] = args.label
    if args.waiting_on is not None:
        changes["waiting_on"] = args.waiting_on
    body = None
    if args.body_file:
        try:
            body = args.body_file.read_text(encoding="utf-8")
        except OSError as exc:
            print(str(exc), file=sys.stderr)
            return 2
    if not changes and body is None:
        print("至少提供一个需要更新的字段或正文文件。", file=sys.stderr)
        return 2
    try:
        story = storage.update_story(
            home,
            args.project_id,
            args.story_id,
            changes,
            body=body,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    metadata = story["metadata"]
    print(f"Story 已更新：{metadata['id']} · {metadata['status']} · {metadata['priority']}")
    return 0


def story_archive(home: Path, project_id: str, story_id: str) -> int:
    try:
        story = storage.archive_story(home, project_id, story_id)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(f"Story 已归档：{story['metadata']['id']}")
    return 0


def doctor(home: Path) -> int:
    storage.ensure_home(home)
    checks = {
        "python3": sys.version.split()[0],
        "tmux": shutil.which("tmux"),
        "codex": shutil.which("codex"),
        "claude": shutil.which("claude"),
        "home": str(home),
        "activation": str(storage.activation_path(home)),
    }
    failed = False
    for name, value in checks.items():
        ok = bool(value)
        print(f"{'✓' if ok else '✗'} {name}: {value or '未找到'}")
        if name in {"tmux", "python3"} and not ok:
            failed = True
    if not checks["codex"] and not checks["claude"]:
        print("✗ 至少需要一个可用的交互式 Agent TUI")
        failed = True
    print("检查不会更新 Codex、Claude Code、模型或认证配置。")
    return 1 if failed else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="perpetuum")
    parser.add_argument("--home", type=Path, help="覆盖默认的 ~/.perpetuum")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init", help="初始化运行时目录")

    start = subparsers.add_parser("start", help="启动 Runner 和前端")
    start.add_argument("--host")
    start.add_argument("--port", type=int)

    stop = subparsers.add_parser("stop", help="停止服务")
    stop.add_argument("--force", action="store_true")

    restart = subparsers.add_parser("restart", help="重启服务")
    restart.add_argument("--host")
    restart.add_argument("--port", type=int)

    status = subparsers.add_parser("status", help="查看整体状态")
    status.add_argument("--json", action="store_true")

    subparsers.add_parser("doctor", help="检查本地依赖")

    project = subparsers.add_parser("project", help="管理项目")
    project_subparsers = project.add_subparsers(dest="project_command", required=True)

    add = project_subparsers.add_parser("add", help="注册项目")
    add.add_argument("path", type=Path)
    add.add_argument("--id")
    add.add_argument("--name")
    add.add_argument("--agent", choices=("codex", "claude"))
    add.add_argument("--timezone", default="Asia/Shanghai")
    add.add_argument(
        "--cron",
        action="append",
        required=True,
        help="标准五字段 cron；需要多个计划时重复传入",
    )

    list_parser = project_subparsers.add_parser("list", help="列出项目")
    list_parser.add_argument("--json", action="store_true")

    for action, help_text in (
        ("pause", "暂停项目的新 Story"),
        ("resume", "恢复项目"),
        ("run", "立即触发项目"),
    ):
        action_parser = project_subparsers.add_parser(action, help=help_text)
        action_parser.add_argument("project_id")

    schedule = project_subparsers.add_parser("schedule", help="设置项目 cron 计划")
    schedule.add_argument("project_id")
    schedule.add_argument("crons", nargs="+", help="标准五字段 cron，参数需要加引号")
    schedule.add_argument("--timezone")

    story = subparsers.add_parser("story", help="管理 Story 看板")
    story_subparsers = story.add_subparsers(dest="story_command", required=True)

    story_list_parser = story_subparsers.add_parser("list", help="只列出 Story 元数据")
    story_list_parser.add_argument("project_id")
    story_list_parser.add_argument("--json", action="store_true")

    story_show_parser = story_subparsers.add_parser("show", help="读取一个 Story")
    story_show_parser.add_argument("project_id")
    story_show_parser.add_argument("story_id")
    story_show_parser.add_argument("--json", action="store_true")

    story_create_parser = story_subparsers.add_parser("create", help="创建 Story")
    story_create_parser.add_argument("project_id")
    story_create_parser.add_argument("--id")
    story_create_parser.add_argument("--title", required=True)
    story_create_parser.add_argument("--summary", required=True)
    story_create_parser.add_argument("--status", choices=storage.STORY_STATUSES, default="ready")
    story_create_parser.add_argument("--priority", choices=storage.STORY_PRIORITIES, default="P1")
    story_create_parser.add_argument("--label", action="append", default=[])
    story_create_parser.add_argument("--body-file", type=Path)

    story_update_parser = story_subparsers.add_parser("update", help="更新 Story")
    story_update_parser.add_argument("project_id")
    story_update_parser.add_argument("story_id")
    story_update_parser.add_argument("--title")
    story_update_parser.add_argument("--summary")
    story_update_parser.add_argument("--status", choices=storage.STORY_STATUSES)
    story_update_parser.add_argument("--priority", choices=storage.STORY_PRIORITIES)
    story_update_parser.add_argument("--label", action="append")
    story_update_parser.add_argument("--waiting-on", choices=("human", "control", "external"))
    story_update_parser.add_argument("--body-file", type=Path)

    story_archive_parser = story_subparsers.add_parser("archive", help="归档 Story")
    story_archive_parser.add_argument("project_id")
    story_archive_parser.add_argument("story_id")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    home = storage.runtime_home(args.home)

    if args.command == "init":
        storage.ensure_home(home)
        print(f"Perpetuum 运行时已初始化：{home}")
        return
    if args.command == "start":
        raise SystemExit(start_service(home, args.host, args.port))
    if args.command == "stop":
        raise SystemExit(stop_service(home, args.force))
    if args.command == "restart":
        raise SystemExit(restart_service(home, args.host, args.port))
    if args.command == "status":
        raise SystemExit(print_status(home, args.json))
    if args.command == "doctor":
        raise SystemExit(doctor(home))
    if args.command == "project":
        if args.project_command == "add":
            raise SystemExit(project_add(args, home))
        if args.project_command == "list":
            raise SystemExit(project_list(home, args.json))
        if args.project_command == "schedule":
            raise SystemExit(
                project_schedule(
                    home,
                    args.project_id,
                    args.crons,
                    args.timezone,
                )
            )
        raise SystemExit(
            project_control(home, args.project_id, args.project_command)
        )
    if args.command == "story":
        if args.story_command == "list":
            raise SystemExit(story_list(home, args.project_id, args.json))
        if args.story_command == "show":
            raise SystemExit(story_show(home, args.project_id, args.story_id, args.json))
        if args.story_command == "create":
            raise SystemExit(story_create(args, home))
        if args.story_command == "update":
            raise SystemExit(story_update(args, home))
        if args.story_command == "archive":
            raise SystemExit(story_archive(home, args.project_id, args.story_id))


if __name__ == "__main__":
    main()
