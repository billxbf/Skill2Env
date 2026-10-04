from datetime import datetime, timedelta, timezone
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from perpetuum_app import storage
from perpetuum_app.runner import Runner


class RunnerTests(unittest.TestCase):
    def make_project(self, root, name="project"):
        home = root / "home"
        project = root / name
        project.mkdir()
        project_id = storage.register_project(
            home,
            project,
            name=name,
            agent="codex",
            crons=["* * * * *"],
        )
        return home, project_id

    def make_active(self, runner, project_id):
        project = runner.project_payload(project_id)
        session = f"perpetuum-project-{project_id[:32]}-20260812-120000-a1b2c3"
        run_dir, dispatch, receipt, run_id = runner.create_run(
            "project",
            session,
            {
                "project": project,
                "trigger": {"reason": "manual", "triggered_at": storage.utc_now()},
            },
        )
        active = {
            "role": "project",
            "run_id": run_id,
            "session": session,
            "project_id": project_id,
            "dispatch_path": str(dispatch),
            "receipt_path": str(receipt),
            "run_dir": str(run_dir),
        }
        return active, run_dir, receipt

    def write_project_state(
        self,
        home,
        project_id,
        *,
        status,
        current_story,
        active_sessions,
        last_activity_at,
    ):
        storage.write_json(
            storage.project_dir(home, project_id) / "runtime" / "state.json",
            {
                "version": 1,
                "status": status,
                "current_story": current_story,
                "story_phase": None,
                "active_sessions": active_sessions,
                "last_activity_at": last_activity_at,
                "last_result": "test",
            },
        )

    def test_receipt_completes_project_session_without_screen_parsing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            project = runner.project_payload(project_id)
            session = f"perpetuum-project-{project_id[:32]}-20260812-120000-a1b2c3"
            run_dir, dispatch, receipt, run_id = runner.create_run(
                "project",
                session,
                {
                    "project": project,
                    "trigger": {"reason": "manual", "triggered_at": storage.utc_now()},
                },
            )
            storage.write_json(
                receipt,
                {
                    "status": "completed",
                    "summary": "完成",
                    "project_id": project_id,
                    "finished_at": storage.utc_now(),
                },
            )
            active = {
                "role": "project",
                "run_id": run_id,
                "session": session,
                "project_id": project_id,
                "dispatch_path": str(dispatch),
                "receipt_path": str(receipt),
                "run_dir": str(run_dir),
            }

            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=True,
            ), mock.patch("perpetuum_app.runner.sessions.kill_session") as kill:
                completed = runner.reconcile_active(
                    active,
                    [project_id],
                )

            self.assertTrue(completed)
            self.assertFalse(run_dir.exists())
            kill.assert_called_once_with(session)

    def test_project_dispatch_only_exposes_relevant_playbooks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            project = runner.project_payload(project_id)
            session = f"perpetuum-project-{project_id[:32]}-20260812-120000-a1b2c3"
            _run_dir, dispatch_path, _receipt, _run_id = runner.create_run(
                "project",
                session,
                {
                    "project": project,
                    "trigger": {"reason": "manual", "triggered_at": storage.utc_now()},
                },
            )

            dispatch = storage.read_json(dispatch_path)
            self.assertEqual(dispatch["carrier_session"], session)
            self.assertEqual(dispatch["project"]["id"], project_id)
            self.assertIn("project_supervisor", dispatch["references"])
            self.assertIn("story_supervisor", dispatch["references"])
            self.assertNotIn("root_supervisor", dispatch["references"])

    def test_project_payload_ignores_agent_command_field(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            project_path = storage.project_dir(home, project_id) / "project.yaml"
            project = storage.read_json(project_path)
            project["agent"]["command"] = "codex --unexpected"
            storage.write_json(project_path, project)

            payload = Runner(home).project_payload(project_id)

            self.assertEqual(payload["agent"], {"kind": "codex"})

    def test_project_session_uses_runner_managed_interactive_agent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            command = [
                "/opt/bin/codex",
                "--no-alt-screen",
                "--dangerously-bypass-approvals-and-sandbox",
            ]
            session = f"perpetuum-project-{project_id[:32]}-20260811-120000-a1b2c3"

            with mock.patch(
                "perpetuum_app.runner.sessions.agent_command",
                return_value=command,
            ) as build_command, mock.patch(
                "perpetuum_app.runner.sessions.session_name",
                return_value=session,
            ), mock.patch(
                "perpetuum_app.runner.sessions.launch_session",
                return_value=session,
            ) as launch:
                active = runner.launch_project(
                    project_id,
                    {"reason": "manual", "triggered_at": storage.utc_now()},
                    storage.ensure_home(home),
                )

            self.assertIsNotNone(active)
            build_command.assert_called_once_with("codex")
            self.assertEqual(launch.call_args.kwargs["command"], command)
            self.assertEqual(launch.call_args.kwargs["role"], "project")
            self.assertEqual(launch.call_args.kwargs["name"], session)

    def test_project_prompt_has_hard_envelope_and_soft_story_decision(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            project = runner.project_payload(project_id)
            prompt = runner.build_project_prompt(
                Path("/tmp/dispatch.json"),
                Path("/tmp/receipt.json"),
                "perpetuum-project-demo-20260812-120000-a1b2c3",
                project,
                {
                    "reason": "cron",
                    "matched_cron": "*/5 0-5 * * *",
                    "triggered_at": storage.utc_now(),
                },
            )

            self.assertIn("Project Supervisor", prompt)
            self.assertIn("通过当前安装的 cc-use Skill", prompt)
            self.assertIn("本轮最多推进一张 Story", prompt)
            self.assertIn("当前承载 session", prompt)
            self.assertIn("原子写入", prompt)
            self.assertIn("direct_sessions", prompt)
            self.assertIn("finish", prompt)
            self.assertIn("决定本轮是否值得推进", prompt)
            self.assertIn("team.md", prompt)
            self.assertIn("Validator 和 Explorer 只在契约启用", prompt)
            self.assertNotIn("cc-use finish", prompt)
            self.assertNotIn("codex exec", prompt)

    def test_missing_agent_binary_becomes_project_escalation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)

            with mock.patch(
                "perpetuum_app.runner.sessions.agent_command",
                side_effect=RuntimeError("codex executable not found"),
            ):
                active = runner.launch_project(
                    project_id,
                    {"reason": "manual", "triggered_at": storage.utc_now()},
                    storage.ensure_home(home),
                )

            self.assertIsNone(active)
            escalation = (
                storage.project_dir(home, project_id) / "escalations.md"
            ).read_text()
            self.assertIn("无法启动 Project Supervisor session", escalation)
            self.assertIn("codex executable not found", escalation)

    def test_first_missing_carrier_keeps_active_project_and_run_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            active, run_dir, _receipt = self.make_active(runner, project_id)
            runner.state["active_projects"] = {project_id: active}
            now = datetime(2026, 9, 6, 12, 0, tzinfo=timezone.utc)

            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(
                runner,
                "current_time",
                return_value=now,
            ), mock.patch.object(
                runner,
                "write_control_escalation",
            ) as escalate, mock.patch.object(runner, "event") as event:
                runner.reconcile_projects()

            self.assertIn(project_id, runner.state["active_projects"])
            self.assertEqual(active["carrier_missing_since"], "2026-09-06T12:00:00Z")
            self.assertNotIn("top_session_orphaned_at", active)
            self.assertTrue(run_dir.is_dir())
            escalate.assert_not_called()
            event.assert_called_once_with(
                "top_session_missing",
                role="project",
                run_id=active["run_id"],
                session=active["session"],
                project_ids=[project_id],
            )

    def test_active_child_chain_never_releases_or_starts_settled_grace(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            active, run_dir, _receipt = self.make_active(runner, project_id)
            missing_at = datetime(2026, 9, 6, 12, 0, tzinfo=timezone.utc)

            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(runner, "current_time", return_value=missing_at):
                self.assertFalse(runner.reconcile_active(active, [project_id]))

            self.write_project_state(
                home,
                project_id,
                status="working",
                current_story="S-001",
                active_sessions=["story-session"],
                last_activity_at="2026-09-06T12:06:00Z",
            )
            much_later = missing_at + timedelta(days=2)
            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(
                runner,
                "current_time",
                return_value=much_later,
            ), mock.patch.object(
                runner,
                "write_control_escalation",
            ) as escalate:
                completed = runner.reconcile_active(active, [project_id])

            self.assertFalse(completed)
            self.assertIn("top_session_orphaned_at", active)
            self.assertNotIn("chain_settled_since", active)
            self.assertTrue(run_dir.is_dir())
            escalate.assert_not_called()

    def test_delayed_receipt_completes_after_carrier_is_orphaned(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            active, run_dir, receipt = self.make_active(runner, project_id)
            missing_at = datetime(2026, 9, 6, 12, 0, tzinfo=timezone.utc)

            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(runner, "current_time", return_value=missing_at):
                self.assertFalse(runner.reconcile_active(active, [project_id]))
            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(
                runner,
                "current_time",
                return_value=missing_at + timedelta(minutes=5),
            ):
                self.assertFalse(runner.reconcile_active(active, [project_id]))

            storage.write_json(
                receipt,
                {
                    "status": "completed",
                    "summary": "late completion",
                    "project_id": project_id,
                    "finished_at": "2026-09-06T12:06:00Z",
                },
            )
            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(runner, "write_control_escalation") as escalate:
                completed = runner.reconcile_active(active, [project_id])

            self.assertTrue(completed)
            self.assertFalse(run_dir.exists())
            escalate.assert_not_called()

    def test_settled_chain_releases_after_grace_and_preserves_run_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            active, run_dir, _receipt = self.make_active(runner, project_id)
            missing_at = datetime(2026, 9, 6, 12, 0, tzinfo=timezone.utc)

            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(runner, "current_time", return_value=missing_at):
                self.assertFalse(runner.reconcile_active(active, [project_id]))
            self.write_project_state(
                home,
                project_id,
                status="idle",
                current_story=None,
                active_sessions=[],
                last_activity_at="2026-09-06T12:01:00Z",
            )
            settled_at = missing_at + timedelta(minutes=5)
            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(runner, "current_time", return_value=settled_at):
                self.assertFalse(runner.reconcile_active(active, [project_id]))

            self.assertEqual(active["chain_settled_since"], "2026-09-06T12:05:00Z")
            runner.state["active_projects"] = {project_id: active}
            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(
                runner,
                "current_time",
                return_value=settled_at + timedelta(minutes=5),
            ):
                runner.reconcile_projects()

            self.assertNotIn(project_id, runner.state["active_projects"])
            self.assertTrue(run_dir.is_dir())
            escalation = (
                storage.project_dir(home, project_id) / "escalations.md"
            ).read_text()
            self.assertIn("稳定链路未写入完成回执", escalation)

    def test_recovered_carrier_clears_all_loss_markers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            active, run_dir, _receipt = self.make_active(runner, project_id)
            active.update(
                {
                    "carrier_missing_since": "2026-09-06T12:00:00Z",
                    "top_session_orphaned_at": "2026-09-06T12:05:00Z",
                    "chain_settled_since": "2026-09-06T12:06:00Z",
                }
            )

            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=True,
            ), mock.patch.object(runner, "event") as event:
                completed = runner.reconcile_active(active, [project_id])

            self.assertFalse(completed)
            self.assertTrue(run_dir.is_dir())
            self.assertNotIn("carrier_missing_since", active)
            self.assertNotIn("top_session_orphaned_at", active)
            self.assertNotIn("chain_settled_since", active)
            event.assert_called_once_with(
                "top_session_recovered",
                role="project",
                run_id=active["run_id"],
                session=active["session"],
                project_ids=[project_id],
            )

    def test_idle_state_older_than_carrier_loss_never_releases(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            runner = Runner(home)
            active, run_dir, _receipt = self.make_active(runner, project_id)
            missing_at = datetime(2026, 9, 6, 12, 0, tzinfo=timezone.utc)
            self.write_project_state(
                home,
                project_id,
                status="idle",
                current_story=None,
                active_sessions=[],
                last_activity_at="2026-09-06T11:59:59Z",
            )

            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(runner, "current_time", return_value=missing_at):
                self.assertFalse(runner.reconcile_active(active, [project_id]))
            with mock.patch(
                "perpetuum_app.runner.sessions.session_exists",
                return_value=False,
            ), mock.patch.object(
                runner,
                "current_time",
                return_value=missing_at + timedelta(days=7),
            ), mock.patch.object(
                runner,
                "write_control_escalation",
            ) as escalate:
                completed = runner.reconcile_active(active, [project_id])

            self.assertFalse(completed)
            self.assertNotIn("chain_settled_since", active)
            self.assertTrue(run_dir.is_dir())
            escalate.assert_not_called()

    def test_due_projects_launch_independently_in_same_tick(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, first = self.make_project(root, "first")
            _home, second = self.make_project(root, "second")
            runner = Runner(home)

            def active(project_id, trigger, config):
                del config
                return {
                    "role": "project",
                    "project_id": project_id,
                    "session": f"session-{project_id}",
                    "trigger": trigger,
                }

            with mock.patch.object(
                runner,
                "launch_project",
                side_effect=active,
            ) as launch:
                runner.tick()

            self.assertEqual(launch.call_count, 2)
            self.assertEqual(set(runner.state["active_projects"]), {first, second})

    def test_active_project_does_not_block_another_project(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, first = self.make_project(root, "first")
            _home, second = self.make_project(root, "second")
            runner = Runner(home)
            runner.state["active_projects"] = {
                first: {
                    "role": "project",
                    "project_id": first,
                    "session": f"perpetuum-project-{first[:32]}-20260812-120000-a1b2c3",
                }
            }

            with mock.patch.object(
                runner,
                "reconcile_projects",
            ), mock.patch.object(
                runner,
                "launch_project",
                return_value={
                    "role": "project",
                    "project_id": second,
                    "session": "second-session",
                },
            ) as launch:
                runner.tick()

            launch.assert_called_once()
            self.assertEqual(launch.call_args.args[0], second)

    def test_corrupt_run_directory_is_not_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home, project_id = self.make_project(root)
            protected = root / "protected"
            protected.mkdir()
            marker = protected / "keep.txt"
            marker.write_text("keep")
            runner = Runner(home)
            active = {
                "role": "project",
                "run_id": "corrupt",
                "session": "unrelated-session",
                "project_id": project_id,
                "dispatch_path": str(protected / "dispatch.json"),
                "receipt_path": str(protected / "receipt.json"),
                "run_dir": str(protected),
            }

            completed = runner.reconcile_active(
                active,
                [project_id],
            )

            self.assertTrue(completed)
            self.assertEqual(marker.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
