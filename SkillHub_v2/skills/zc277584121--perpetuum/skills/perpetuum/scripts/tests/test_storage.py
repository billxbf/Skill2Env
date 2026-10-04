import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from perpetuum_app import storage


class StorageTests(unittest.TestCase):
    def test_register_project_creates_self_contained_harness(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            project = root / "project"
            project.mkdir()

            project_id = storage.register_project(
                home,
                project,
                name="测试项目",
                agent="codex",
                crons=["*/5 0-5 * * *"],
                timezone_name="Asia/Shanghai",
            )
            harness = storage.project_dir(home, project_id)

            self.assertTrue((home / "activation.yaml").is_file())
            self.assertTrue((harness / "project.yaml").is_file())
            self.assertTrue((harness / "schedule.yaml").is_file())
            self.assertTrue((harness / "goal.md").is_file())
            self.assertTrue((harness / "team.md").is_file())
            self.assertTrue((harness / "stories").is_dir())
            self.assertTrue((harness / "history.md").is_file())
            self.assertTrue((harness / "inbox.md").is_file())
            self.assertTrue((harness / "questions.md").is_file())
            self.assertTrue((harness / "escalations.md").is_file())
            self.assertTrue((harness / "runtime" / "state.json").is_file())
            self.assertTrue((harness / "runtime" / "events.log").is_file())

            runtime = storage.read_json(harness / "runtime" / "state.json")
            self.assertEqual(runtime["version"], 1)
            self.assertIsNone(runtime["current_story"])

            activation = json.loads((home / "activation.yaml").read_text())
            project_config = json.loads((harness / "project.yaml").read_text())
            self.assertEqual(project_config["agent"], {"kind": "codex"})
            schedule = storage.load_project_schedule(home, project_id)
            self.assertEqual(
                schedule["cron"],
                ["*/5 0-5 * * *"],
            )
            self.assertEqual(schedule["timezone"], "Asia/Shanghai")
            self.assertIn("registered_at", activation["projects"][project_id])
            self.assertIn("Executor（必选）", (harness / "team.md").read_text())

    def test_human_message_is_appended(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inbox.md"
            storage.append_human_message(path, "前端指令", "优先检查网络")
            content = path.read_text()
            self.assertIn("前端指令", content)
            self.assertIn("优先检查网络", content)

    def test_project_id_distinguishes_same_directory_name(self):
        first = storage.project_id_for_path(Path("/a/project"))
        second = storage.project_id_for_path(Path("/b/project"))
        self.assertNotEqual(first, second)

    def test_story_front_matter_round_trip_and_progressive_list(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            project = root / "project"
            project.mkdir()
            project_id = storage.register_project(home, project)

            created = storage.create_story(
                home,
                project_id,
                "完成可复现实验",
                "交付质量、资源和验证结论",
                priority="P0",
                labels=["benchmark", "research"],
                body="# 验收标准\n\n结果可以独立复算。",
            )
            story_id = created["metadata"]["id"]

            stories = storage.list_stories(home, project_id)
            self.assertEqual(len(stories), 1)
            self.assertEqual(stories[0]["id"], story_id)
            self.assertEqual(stories[0]["priority"], "P0")
            self.assertNotIn("body", stories[0])

            loaded = storage.load_story(home, project_id, story_id)
            self.assertIn("独立复算", loaded["body"])
            self.assertEqual(loaded["metadata"]["labels"], ["benchmark", "research"])

            updated = storage.update_story(
                home,
                project_id,
                story_id,
                {
                    "status": "waiting",
                    "waiting_on": "human",
                    "question_ids": ["Q-1"],
                },
            )
            self.assertEqual(updated["metadata"]["status"], "waiting")
            self.assertEqual(updated["metadata"]["waiting_on"], "human")

            resumed = storage.update_story(
                home,
                project_id,
                story_id,
                {"status": "ready"},
            )
            self.assertEqual(resumed["metadata"]["status"], "ready")
            self.assertNotIn("waiting_on", resumed["metadata"])

    def test_list_stories_rejects_unknown_project(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "未知项目"):
                storage.list_stories(Path(directory), "missing")

    def test_story_file_name_must_match_front_matter_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            project = root / "project"
            project.mkdir()
            project_id = storage.register_project(home, project)
            path = storage.stories_dir(home, project_id) / "S-001.md"
            path.write_text(
                "---\nid: S-002\ntitle: 标题\nsummary: 摘要\nstatus: ready\n"
                "priority: P1\nlabels: []\n---\n\n正文\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "文件名"):
                storage.list_stories(home, project_id)

    def test_story_board_keeps_latest_completed_cards_and_archives_overflow(self):
        stories = []
        for index in range(43):
            stories.append(
                {
                    "id": f"S-{index:03d}",
                    "status": "done",
                    "completed_at": f"2026-08-{index + 1:02d}T00:00:00Z",
                }
            )
        stories.append({"id": "S-READY", "status": "ready"})
        stories.append({"id": "S-CANCELLED", "status": "cancelled"})

        board, archived = storage.partition_stories_for_board(stories, 40)

        self.assertEqual(len([story for story in board if story["status"] == "done"]), 40)
        self.assertIn("S-READY", {story["id"] for story in board})
        self.assertEqual(len(archived), 4)
        self.assertEqual(
            {story["archive_reason"] for story in archived},
            {"completed_overflow", "cancelled"},
        )
        self.assertTrue(all(story["status"] == "done" for story in archived if story["id"] != "S-CANCELLED"))

    def test_manual_archive_preserves_done_status(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            project = root / "project"
            project.mkdir()
            project_id = storage.register_project(home, project)
            story = storage.create_story(
                home,
                project_id,
                "完成结果",
                "保留完成事实",
                status="done",
            )

            archived = storage.archive_story(home, project_id, story["metadata"]["id"])

            self.assertEqual(archived["metadata"]["status"], "done")
            self.assertIn("archived_at", archived["metadata"])
            board, history = storage.partition_stories_for_board(
                storage.list_stories(home, project_id)
            )
            self.assertEqual(board, [])
            self.assertEqual(history[0]["archive_reason"], "manual")

    def test_manual_archive_rejects_unfinished_story(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            project = root / "project"
            project.mkdir()
            project_id = storage.register_project(home, project)
            story = storage.create_story(home, project_id, "待办", "尚未完成")

            with self.assertRaisesRegex(ValueError, "只有已完成"):
                storage.archive_story(home, project_id, story["metadata"]["id"])

    def test_project_schedule_can_be_updated(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            project = root / "project"
            project.mkdir()
            project_id = storage.register_project(home, project)

            storage.set_project_schedule(
                home,
                project_id,
                ["*/5 0-5 * * *", "0 18 * * 1-5"],
                "UTC",
            )

            schedule = storage.load_project_schedule(home, project_id)
            self.assertEqual(
                schedule["cron"],
                ["*/5 0-5 * * *", "0 18 * * 1-5"],
            )
            self.assertEqual(schedule["timezone"], "UTC")

    def test_claude_environment_takes_priority(self):
        with mock.patch.dict(
            os.environ,
            {"CLAUDECODE": "1", "CODEX_HOME": "/tmp/codex"},
            clear=True,
        ):
            self.assertEqual(storage.detect_agent_kind(), "claude")


if __name__ == "__main__":
    unittest.main()
