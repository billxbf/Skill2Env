"""Local HTTP API and static frontend."""

from __future__ import annotations

import json
import mimetypes
import os
import re
import threading
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import unquote, urlparse

from . import scheduler, storage


PROJECT_PATH = re.compile(r"^/api/projects/([^/]+)(?:/(inbox|response|control))?$")
STORY_PATH = re.compile(r"^/api/projects/([^/]+)/stories(?:/([^/]+))?$")
DOCUMENT_PATH = re.compile(r"^/api/projects/([^/]+)/documents/([^/]+)$")
PROJECT_DOCUMENTS = {
    "goal": ("goal.md", 100_000),
    "team": ("team.md", 100_000),
    "history": ("history.md", 200_000),
    "inbox": ("inbox.md", 100_000),
    "questions": ("questions.md", 100_000),
    "escalations": ("escalations.md", 100_000),
    "events": ("runtime/events.log", 200_000),
}


def process_alive(pid: Any) -> bool:
    if not isinstance(pid, int) or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def project_summary(
    home: Path,
    project_id: str,
    runner_state: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    project = storage.load_project(home, project_id) or {}
    state = storage.load_project_state(home, project_id)
    try:
        schedule = storage.load_project_schedule(home, project_id)
        schedule_view = scheduler.schedule_view(schedule)
    except ValueError as exc:
        schedule = {
            "version": 1,
            "timezone": "",
            "enabled": False,
            "paused": True,
            "force_run": False,
            "cron": [],
            "error": str(exc),
        }
        schedule_view = {
            "description": "运行计划无效",
            "simple": None,
            "next_run_at": None,
        }
    active_projects = (runner_state or {}).get("active_projects", {})
    active = (
        active_projects.get(project_id)
        if isinstance(active_projects, dict)
        else None
    )
    return {
        "id": project_id,
        "name": project.get("name", project_id),
        "path": project.get("path", ""),
        "agent": project.get("agent", {}),
        "status": state.get("status", "unknown"),
        "current_story": state.get("current_story"),
        "story_phase": state.get("story_phase"),
        "last_activity_at": state.get("last_activity_at"),
        "last_result": state.get("last_result"),
        "paused": bool(schedule.get("paused", False)),
        "enabled": bool(schedule.get("enabled", True)),
        "schedule": schedule,
        "schedule_view": schedule_view,
        "project_session": active.get("session") if isinstance(active, dict) else None,
    }


def section_content(markdown: str, heading: str) -> str:
    lines = markdown.replace("\r\n", "\n").split("\n")
    marker = f"## {heading}"
    try:
        start = next(index for index, line in enumerate(lines) if line.strip() == marker)
    except StopIteration:
        return ""
    result = []
    for line in lines[start + 1 :]:
        if re.match(r"^#{1,2}\s+", line):
            break
        result.append(line)
    return "\n".join(result).strip()


def has_pending_content(markdown: str, heading: str) -> bool:
    content = section_content(markdown, heading)
    normalized = re.sub(r"[-*#`\s]", "", content.replace("暂无。", "").replace("暂无", ""))
    return bool(normalized)


def global_status(home: Path) -> Dict[str, Any]:
    activation = storage.ensure_home(home)
    runner_state = storage.read_json(
        storage.runner_state_path(home),
        storage.default_runner_state(),
    )
    service = runner_state.get("service", {})
    service["alive"] = process_alive(service.get("pid"))
    projects = [
        project_summary(home, project_id, runner_state)
        for project_id in storage.list_project_ids(home)
    ]
    return {
        "home": str(home),
        "activation": activation,
        "runner": runner_state,
        "projects": projects,
    }


def project_detail(home: Path, project_id: str) -> Dict[str, Any]:
    activation = storage.ensure_home(home)
    if project_id not in activation.get("projects", {}):
        raise KeyError(project_id)
    harness = storage.project_dir(home, project_id)
    questions = storage.read_text(harness / "questions.md", limit=100_000)
    escalations = storage.read_text(harness / "escalations.md", limit=100_000)
    stories = storage.list_stories(home, project_id)
    board_stories, archived_stories = storage.partition_stories_for_board(stories)
    return {
        "summary": project_summary(
            home,
            project_id,
            storage.read_json(
                storage.runner_state_path(home),
                storage.default_runner_state(),
            ),
        ),
        "project": storage.load_project(home, project_id),
        "runtime": storage.load_project_state(home, project_id),
        "stories": board_stories,
        "archived_stories": archived_stories,
        "visible_done_limit": storage.DEFAULT_VISIBLE_DONE_LIMIT,
        "attention": {
            "questions": has_pending_content(questions, "待人类回答"),
            "escalations": has_pending_content(escalations, "待处理"),
        },
    }


def project_document(home: Path, project_id: str, key: str) -> Dict[str, str]:
    if storage.load_project(home, project_id) is None:
        raise KeyError(project_id)
    definition = PROJECT_DOCUMENTS.get(key)
    if definition is None:
        raise ValueError(f"未知项目文档：{key}")
    relative_path, limit = definition
    return {
        "key": key,
        "path": relative_path,
        "content": storage.read_text(
            storage.project_dir(home, project_id) / relative_path,
            limit=limit,
        ),
    }


def read_body(handler: BaseHTTPRequestHandler) -> Dict[str, Any]:
    length = int(handler.headers.get("Content-Length", "0"))
    if length <= 0 or length > 1_000_000:
        raise ValueError("请求内容为空或过大")
    raw = handler.rfile.read(length)
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict):
        raise ValueError("请求必须是 JSON 对象")
    return value


def handler_factory(home: Path) -> Any:
    static_root = Path(__file__).resolve().parent / "frontend"

    class Handler(BaseHTTPRequestHandler):
        server_version = "Perpetuum/0.3"

        def log_message(self, format_string: str, *args: Any) -> None:
            del format_string, args

        def send_json(self, value: Any, status: int = 200) -> None:
            data = json.dumps(value, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def send_error_json(self, status: int, message: str) -> None:
            self.send_json({"ok": False, "error": message}, status)

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            if parsed.path == "/api/status":
                self.send_json(global_status(home))
                return
            document_match = DOCUMENT_PATH.fullmatch(parsed.path)
            if document_match:
                try:
                    self.send_json(
                        project_document(
                            home,
                            unquote(document_match.group(1)),
                            unquote(document_match.group(2)),
                        )
                    )
                except KeyError:
                    self.send_error_json(HTTPStatus.NOT_FOUND, "项目不存在")
                except ValueError as exc:
                    self.send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            story_match = STORY_PATH.fullmatch(parsed.path)
            if story_match and story_match.group(2):
                try:
                    self.send_json(
                        storage.load_story(
                            home,
                            unquote(story_match.group(1)),
                            unquote(story_match.group(2)),
                        )
                    )
                except ValueError as exc:
                    self.send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            match = PROJECT_PATH.fullmatch(parsed.path)
            if match and not match.group(2):
                try:
                    self.send_json(project_detail(home, unquote(match.group(1))))
                except KeyError:
                    self.send_error_json(HTTPStatus.NOT_FOUND, "项目不存在")
                except ValueError as exc:
                    self.send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self.serve_static(parsed.path)

        def do_POST(self) -> None:
            parsed = urlparse(self.path)
            story_match = STORY_PATH.fullmatch(parsed.path)
            if story_match:
                project_id = unquote(story_match.group(1))
                story_id = unquote(story_match.group(2)) if story_match.group(2) else None
                try:
                    body = read_body(self)
                    if storage.load_project(home, project_id) is None:
                        raise KeyError(project_id)
                    if story_id:
                        changes = {
                            key: body[key]
                            for key in storage.STORY_MUTABLE_FIELDS
                            if key in body
                        }
                        story = storage.update_story(
                            home,
                            project_id,
                            story_id,
                            changes,
                            body=str(body["body"]) if "body" in body else None,
                        )
                        event = "story_updated"
                    else:
                        story = storage.create_story(
                            home,
                            project_id,
                            str(body.get("title", "")),
                            str(body.get("summary", "")),
                            story_id=str(body["id"]) if body.get("id") else None,
                            status=str(body.get("status", "ready")),
                            priority=str(body.get("priority", "P1")),
                            labels=body.get("labels") if isinstance(body.get("labels"), list) else [],
                            body=str(body["body"]) if "body" in body else None,
                        )
                        event = "story_created"
                    storage.append_event(
                        storage.project_dir(home, project_id) / "runtime" / "events.log",
                        event,
                        story_id=story["metadata"]["id"],
                        source="frontend",
                    )
                    self.send_json({"ok": True, "story": story})
                except KeyError:
                    self.send_error_json(HTTPStatus.NOT_FOUND, "项目不存在")
                except (ValueError, json.JSONDecodeError) as exc:
                    self.send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                except OSError as exc:
                    self.send_error_json(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))
                return
            match = PROJECT_PATH.fullmatch(parsed.path)
            if not match or not match.group(2):
                self.send_error_json(HTTPStatus.NOT_FOUND, "接口不存在")
                return
            project_id = unquote(match.group(1))
            action = match.group(2)
            try:
                body = read_body(self)
                if storage.load_project(home, project_id) is None:
                    raise KeyError(project_id)
                if action == "inbox":
                    storage.append_human_message(
                        storage.project_dir(home, project_id) / "inbox.md",
                        "前端指令",
                        str(body.get("text", "")),
                    )
                    storage.append_event(
                        storage.runner_events_path(home),
                        "human_message_added",
                        project_id=project_id,
                        channel="inbox",
                    )
                elif action == "response":
                    channel = str(body.get("channel", "questions"))
                    if channel not in {"questions", "escalations"}:
                        raise ValueError("回复通道必须是 questions 或 escalations")
                    storage.append_human_message(
                        storage.project_dir(home, project_id) / f"{channel}.md",
                        "人类回复",
                        str(body.get("text", "")),
                    )
                    storage.append_event(
                        storage.runner_events_path(home),
                        "human_message_added",
                        project_id=project_id,
                        channel=channel,
                    )
                elif action == "control":
                    control_action = str(body.get("action", ""))
                    if control_action == "schedule":
                        mode = str(body.get("mode", "cron"))
                        if mode == "simple":
                            crons = scheduler.crons_from_simple(body.get("simple"))
                        elif mode == "cron":
                            crons = body.get("cron", [])
                            if not isinstance(crons, list):
                                raise ValueError("cron 必须是列表")
                        else:
                            raise ValueError("运行计划模式必须是 simple 或 cron")
                        timezone_name = body.get("timezone")
                        storage.set_project_schedule(
                            home,
                            project_id,
                            crons,
                            str(timezone_name) if timezone_name else None,
                        )
                    else:
                        storage.update_project_control(
                            home,
                            project_id,
                            control_action,
                        )
                self.send_json({"ok": True})
            except KeyError:
                self.send_error_json(HTTPStatus.NOT_FOUND, "项目不存在")
            except (ValueError, json.JSONDecodeError) as exc:
                self.send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
            except OSError as exc:
                self.send_error_json(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))

        def serve_static(self, request_path: str) -> None:
            relative = "index.html" if request_path == "/" else request_path.lstrip("/")
            candidate = (static_root / relative).resolve()
            if static_root not in candidate.parents and candidate != static_root:
                self.send_error_json(HTTPStatus.FORBIDDEN, "禁止访问")
                return
            if not candidate.is_file():
                self.send_error_json(HTTPStatus.NOT_FOUND, "页面不存在")
                return
            data = candidate.read_bytes()
            content_type = mimetypes.guess_type(str(candidate))[0] or "application/octet-stream"
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return Handler


class RuntimeServer:
    def __init__(self, home: Path, host: str, port: int) -> None:
        self.server = ThreadingHTTPServer((host, port), handler_factory(home))
        self.thread: Optional[threading.Thread] = None

    def start(self) -> None:
        self.thread = threading.Thread(
            target=self.server.serve_forever,
            name="perpetuum-http",
            daemon=True,
        )
        self.thread.start()

    def stop(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        if self.thread is not None:
            self.thread.join(timeout=5)
