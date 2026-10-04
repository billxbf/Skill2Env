"""Top-level tmux session management."""

from __future__ import annotations

import re
import secrets
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Sequence


AGENT_ARGUMENTS = {
    "codex": ["--no-alt-screen", "--dangerously-bypass-approvals-and-sandbox"],
    "claude": ["--dangerously-skip-permissions"],
}


def agent_command(kind: str) -> List[str]:
    if kind not in AGENT_ARGUMENTS:
        raise RuntimeError(f"不支持的 Agent 类型：{kind}")
    executable = shutil.which(kind)
    if not executable:
        raise RuntimeError(f"找不到 Agent 命令：{kind}")
    return [executable, *AGENT_ARGUMENTS[kind]]


def session_name(role: str, identity: Optional[str] = None) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    suffix = ""
    if identity:
        safe_identity = re.sub(r"[^a-zA-Z0-9_-]+", "-", identity).strip("-_")
        if safe_identity:
            suffix = f"-{safe_identity[:32]}"
    return f"perpetuum-{role}{suffix}-{stamp}-{secrets.token_hex(3)}"


def session_exists(name: str) -> bool:
    return (
        subprocess.run(
            ["tmux", "has-session", "-t", f"={name}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def is_owned_top_session(name: str, role: str) -> bool:
    if role != "project":
        return False
    return bool(
        re.fullmatch(
            r"perpetuum-project-[A-Za-z0-9_-]{1,32}-\d{8}-\d{6}-[0-9a-f]{6}",
            name,
        )
    )


def capture_session(name: str, lines: int = 200) -> str:
    result = subprocess.run(
        ["tmux", "capture-pane", "-t", f"={name}:0.0", "-p", "-S", f"-{lines}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    return result.stdout


def kill_session(name: str) -> None:
    subprocess.run(
        ["tmux", "kill-session", "-t", f"={name}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )


def launch_session(
    role: str,
    command: Sequence[str],
    cwd: Path,
    prompt: str,
    startup_seconds: int = 8,
    kind: str = "codex",
    name: Optional[str] = None,
) -> str:
    name = name or session_name(role)
    argv = list(command)
    if not argv:
        raise RuntimeError("Agent 启动命令为空")

    result = subprocess.run(
        [
            "tmux",
            "new-session",
            "-d",
            "-s",
            name,
            "-x",
            "200",
            "-y",
            "60",
            "-c",
            str(cwd),
            *argv,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "无法创建 tmux session")

    time.sleep(max(1, startup_seconds))
    if not session_exists(name):
        raise RuntimeError("Agent TUI 在接收任务前已经退出")

    try:
        buffer_name = f"pp-{secrets.token_hex(4)}"
        pane_target = f"={name}:0.0"
        load = subprocess.run(
            ["tmux", "load-buffer", "-b", buffer_name, "-"],
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if load.returncode != 0:
            raise RuntimeError(load.stderr.strip() or "无法写入 tmux buffer")

        paste = subprocess.run(
            ["tmux", "paste-buffer", "-d", "-b", buffer_name, "-t", pane_target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if paste.returncode != 0:
            raise RuntimeError(paste.stderr.strip() or "无法投递 tmux buffer")
        if kind == "codex":
            subprocess.run(
                ["tmux", "send-keys", "-t", pane_target, "Escape"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            time.sleep(0.3)
        for key in ("Enter", "C-m", "Enter"):
            sent = subprocess.run(
                ["tmux", "send-keys", "-t", pane_target, key],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
            if sent.returncode != 0:
                raise RuntimeError(sent.stderr.strip() or "无法提交 TUI 输入")
            time.sleep(0.2)
    except Exception:
        kill_session(name)
        raise
    return name
