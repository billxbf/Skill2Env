import json
from pathlib import Path
import tempfile
import unittest
from urllib.request import Request
from urllib.request import urlopen

from perpetuum_app import storage
from perpetuum_app.server import RuntimeServer, has_pending_content


class ServerTests(unittest.TestCase):
    def test_attention_summary_reads_pending_section(self):
        self.assertFalse(
            has_pending_content(
                "# 业务问题\n\n## 待人类回答\n\n暂无。\n\n## 已吸收\n",
                "待人类回答",
            )
        )
        self.assertTrue(
            has_pending_content(
                "# 业务问题\n\n## 待人类回答\n\nQ-1：请选择数据范围。\n\n## 已吸收\n",
                "待人类回答",
            )
        )

    def test_status_and_project_detail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            home = root / "home"
            project = root / "project"
            project.mkdir()
            project_id = storage.register_project(home, project, name="测试项目")
            story = storage.create_story(
                home,
                project_id,
                "完成首个结果",
                "交付可以独立验证的成果",
                priority="P0",
                labels=["research"],
            )
            story_id = story["metadata"]["id"]

            server = RuntimeServer(home, "127.0.0.1", 0)
            port = server.server.server_address[1]
            server.start()
            try:
                with urlopen(f"http://127.0.0.1:{port}/api/status") as response:
                    status = json.loads(response.read())
                self.assertEqual(status["projects"][0]["id"], project_id)
                self.assertNotIn("latest_report", status["projects"][0])
                self.assertEqual(
                    status["projects"][0]["schedule"]["cron"],
                    ["0 0 * * *"],
                )
                self.assertEqual(
                    status["projects"][0]["schedule_view"]["description"],
                    "每天 00:00 启动",
                )
                self.assertIn("next_run_at", status["projects"][0]["schedule_view"])

                with urlopen(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}"
                ) as response:
                    detail = json.loads(response.read())
                self.assertEqual(detail["stories"][0]["id"], story_id)
                self.assertEqual(detail["archived_stories"], [])
                self.assertEqual(detail["visible_done_limit"], 40)
                self.assertNotIn("files", detail)
                self.assertEqual(
                    detail["attention"],
                    {"questions": False, "escalations": False},
                )

                with urlopen(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/documents/goal"
                ) as response:
                    goal = json.loads(response.read())
                self.assertEqual(goal["path"], "goal.md")
                self.assertIn("长期目标", goal["content"])

                with urlopen(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/documents/team"
                ) as response:
                    team = json.loads(response.read())
                self.assertEqual(team["path"], "team.md")
                self.assertIn("Agent 队伍契约", team["content"])

                with urlopen(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/stories/{story_id}"
                ) as response:
                    story_detail = json.loads(response.read())
                self.assertEqual(story_detail["metadata"]["priority"], "P0")
                self.assertIn("验收标准", story_detail["body"])

                request = Request(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/stories/{story_id}",
                    data=json.dumps(
                        {"status": "waiting", "priority": "P1", "labels": ["human"]}
                    ).encode(),
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with urlopen(request) as response:
                    result = json.loads(response.read())
                self.assertTrue(result["ok"])
                updated = storage.load_story(home, project_id, story_id)
                self.assertEqual(updated["metadata"]["status"], "waiting")

                request = Request(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/inbox",
                    data=json.dumps({"text": "优先检查网络"}).encode(),
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with urlopen(request) as response:
                    result = json.loads(response.read())
                self.assertTrue(result["ok"])
                self.assertIn(
                    "优先检查网络",
                    (storage.project_dir(home, project_id) / "inbox.md").read_text(),
                )

                request = Request(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/control",
                    data=json.dumps({"action": "pause"}).encode(),
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with urlopen(request) as response:
                    result = json.loads(response.read())
                self.assertTrue(result["ok"])
                schedule = storage.load_project_schedule(home, project_id)
                self.assertTrue(schedule["paused"])

                request = Request(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/control",
                    data=json.dumps(
                        {
                            "action": "schedule",
                            "timezone": "UTC",
                            "cron": ["*/15 * * * *"],
                        }
                    ).encode(),
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with urlopen(request) as response:
                    result = json.loads(response.read())
                self.assertTrue(result["ok"])
                schedule = storage.load_project_schedule(home, project_id)
                self.assertEqual(schedule["timezone"], "UTC")
                self.assertEqual(schedule["cron"], ["*/15 * * * *"])

                request = Request(
                    f"http://127.0.0.1:{port}/api/projects/{project_id}/control",
                    data=json.dumps(
                        {
                            "action": "schedule",
                            "mode": "simple",
                            "timezone": "Asia/Shanghai",
                            "simple": {
                                "kind": "window",
                                "start": "18:00",
                                "end": "06:00",
                                "interval_minutes": 30,
                            },
                        }
                    ).encode(),
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with urlopen(request) as response:
                    result = json.loads(response.read())
                self.assertTrue(result["ok"])
                schedule = storage.load_project_schedule(home, project_id)
                self.assertEqual(schedule["timezone"], "Asia/Shanghai")
                self.assertEqual(schedule["cron"], ["*/30 0-5,18-23 * * *"])
            finally:
                server.stop()


if __name__ == "__main__":
    unittest.main()
