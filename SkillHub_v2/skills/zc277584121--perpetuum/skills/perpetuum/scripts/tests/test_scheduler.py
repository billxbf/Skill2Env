from datetime import datetime, timezone
import unittest

from perpetuum_app import scheduler


class SchedulerTests(unittest.TestCase):
    def schedule(self, expression="*/5 0-5 * * *"):
        return {
            "version": 1,
            "timezone": "Asia/Shanghai",
            "enabled": True,
            "paused": False,
            "force_run": False,
            "cron": [expression],
        }

    def test_cron_matches_project_timezone(self):
        now = datetime(2026, 8, 5, 16, 10, tzinfo=timezone.utc)
        self.assertEqual(
            scheduler.matching_crons(self.schedule(), now),
            ["*/5 0-5 * * *"],
        )

    def test_cron_does_not_match_outside_range(self):
        now = datetime(2026, 8, 6, 2, 10, tzinfo=timezone.utc)
        self.assertEqual(scheduler.matching_crons(self.schedule(), now), [])

    def test_same_cron_minute_only_triggers_once(self):
        now = datetime(2026, 8, 5, 16, 10, tzinfo=timezone.utc)
        first = scheduler.project_trigger(self.schedule(), None, now)
        self.assertIsNotNone(first)
        second = scheduler.project_trigger(
            self.schedule(),
            first["cron_minute"],
            now,
        )
        self.assertIsNone(second)

    def test_force_run_ignores_cron_but_not_pause(self):
        schedule = self.schedule("0 12 * * *")
        schedule["force_run"] = True
        now = datetime(2026, 8, 5, 16, 10, tzinfo=timezone.utc)
        self.assertEqual(
            scheduler.project_trigger(schedule, None, now)["reason"],
            "manual",
        )
        schedule["paused"] = True
        self.assertIsNone(scheduler.project_trigger(schedule, None, now))

    def test_only_standard_five_field_cron_is_accepted(self):
        with self.assertRaisesRegex(ValueError, "标准五字段"):
            scheduler.validate_cron("0 0 0 * * *")

    def test_invalid_timezone_is_rejected(self):
        schedule = self.schedule()
        schedule["timezone"] = "Nowhere/Invalid"
        with self.assertRaisesRegex(ValueError, "无效时区"):
            scheduler.validate_project_schedule(schedule)

    def test_human_window_converts_to_cron_and_back(self):
        crons = scheduler.crons_from_simple(
            {
                "kind": "window",
                "start": "18:00",
                "end": "06:00",
                "interval_minutes": 30,
            }
        )
        self.assertEqual(crons, ["*/30 0-5,18-23 * * *"])
        self.assertEqual(
            scheduler.simple_from_crons(crons),
            {
                "kind": "window",
                "start": "18:00",
                "end": "06:00",
                "interval_minutes": 30,
            },
        )

    def test_existing_split_window_is_presented_as_one_human_schedule(self):
        simple = scheduler.simple_from_crons(
            ["30 15 * * *", "0,30 16 * * *"]
        )
        self.assertEqual(
            simple,
            {
                "kind": "window",
                "start": "15:30",
                "end": "17:00",
                "interval_minutes": 30,
            },
        )
        self.assertEqual(
            scheduler.describe_simple_schedule(simple),
            "每天 15:30–17:00，每 30 分钟启动",
        )

    def test_fixed_time_human_schedule(self):
        self.assertEqual(
            scheduler.crons_from_simple({"kind": "fixed", "time": "09:30"}),
            ["30 9 * * *"],
        )
        self.assertEqual(
            scheduler.simple_from_crons(["30 9 * * *"]),
            {"kind": "fixed", "time": "09:30"},
        )

    def test_next_project_run_uses_project_timezone(self):
        now = datetime(2026, 8, 14, 14, 20, tzinfo=timezone.utc)
        schedule = self.schedule("30 22 * * *")
        self.assertEqual(
            scheduler.next_project_run(schedule, now),
            "2026-08-14T14:30:00Z",
        )

    def test_paused_project_has_no_expected_next_run(self):
        schedule = self.schedule("30 22 * * *")
        schedule["paused"] = True
        self.assertIsNone(scheduler.next_project_run(schedule))

    def test_complex_cron_keeps_advanced_presentation(self):
        schedule = self.schedule("0 9 * * 1-5")
        view = scheduler.schedule_view(schedule)
        self.assertIsNone(view["simple"])
        self.assertEqual(view["description"], "自定义 Cron（1 条）")


if __name__ == "__main__":
    unittest.main()
