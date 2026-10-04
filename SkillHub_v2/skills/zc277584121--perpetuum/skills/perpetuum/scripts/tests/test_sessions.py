from pathlib import Path
import shutil
import tempfile
import time
import unittest
from unittest import mock

from perpetuum_app import sessions


@unittest.skipUnless(shutil.which("tmux"), "tmux is required")
class SessionTests(unittest.TestCase):
    def test_top_level_ownership_only_accepts_project_names(self):
        self.assertTrue(
            sessions.is_owned_top_session(
                "perpetuum-project-demo-20260812-120000-a1b2c3",
                "project",
            )
        )
        self.assertFalse(
            sessions.is_owned_top_session(
                "perpetuum-root-20260812-120000-a1b2c3",
                "root",
            )
        )

    def test_agent_commands_use_resolved_binaries_and_unattended_flags(self):
        binaries = {
            "codex": "/opt/bin/codex",
            "claude": "/opt/bin/claude",
        }
        with mock.patch(
            "perpetuum_app.sessions.shutil.which",
            side_effect=binaries.get,
        ):
            self.assertEqual(
                sessions.agent_command("codex"),
                [
                    "/opt/bin/codex",
                    "--no-alt-screen",
                    "--dangerously-bypass-approvals-and-sandbox",
                ],
            )
            self.assertEqual(
                sessions.agent_command("claude"),
                ["/opt/bin/claude", "--dangerously-skip-permissions"],
            )

    def test_prompt_delivery_uses_unique_tmux_session(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            marker = root / "received.txt"
            session = sessions.launch_session(
                role="smoke",
                command=[shutil.which("bash") or "bash"],
                cwd=root,
                prompt=f"printf delivered > {marker}",
                startup_seconds=1,
                kind="claude",
            )
            try:
                deadline = time.time() + 5
                while time.time() < deadline and not marker.exists():
                    time.sleep(0.1)
                self.assertEqual(marker.read_text(), "delivered")
                self.assertTrue(session.startswith("perpetuum-smoke-"))
            finally:
                sessions.kill_session(session)


if __name__ == "__main__":
    unittest.main()
