"""Cron evaluation for project activation."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from croniter import croniter


SIMPLE_INTERVALS = {5, 10, 15, 20, 30, 60}


def utc_text(value: Optional[datetime] = None) -> str:
    current = value or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    return current.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def timezone_info(timezone_name: str) -> ZoneInfo:
    try:
        return ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as exc:
        raise ValueError(f"无效时区：{timezone_name}") from exc


def local_now(
    timezone_name: str,
    now: Optional[datetime] = None,
) -> datetime:
    zone = timezone_info(timezone_name)
    if now is None:
        return datetime.now(zone)
    if now.tzinfo is None:
        return now.replace(tzinfo=zone)
    return now.astimezone(zone)


def validate_cron(expression: str) -> str:
    value = str(expression).strip()
    if len(value.split()) != 5 or not croniter.is_valid(value):
        raise ValueError(f"无效 cron 表达式：{expression}；请使用标准五字段语法")
    return value


def normalize_crons(expressions: Any) -> List[str]:
    if not isinstance(expressions, list) or not expressions:
        raise ValueError("至少需要一个 cron 表达式")
    result = []
    for expression in expressions:
        value = validate_cron(str(expression))
        if value not in result:
            result.append(value)
    return result


def parse_clock(value: Any, label: str) -> int:
    text = str(value).strip()
    try:
        hour_text, minute_text = text.split(":", 1)
        hour = int(hour_text)
        minute = int(minute_text)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label}必须使用 HH:MM 格式") from exc
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError(f"{label}超出有效时间范围")
    return hour * 60 + minute


def clock_text(value: int) -> str:
    minute = value % (24 * 60)
    return f"{minute // 60:02d}:{minute % 60:02d}"


def compress_numbers(values: List[int]) -> str:
    ordered = sorted(set(values))
    ranges = []
    start = ordered[0]
    end = start
    for value in ordered[1:]:
        if value == end + 1:
            end = value
            continue
        ranges.append(str(start) if start == end else f"{start}-{end}")
        start = end = value
    ranges.append(str(start) if start == end else f"{start}-{end}")
    return ",".join(ranges)


def minute_field(values: List[int]) -> str:
    ordered = sorted(set(values))
    for interval in sorted(SIMPLE_INTERVALS):
        if interval < 60 and ordered == list(range(0, 60, interval)):
            return f"*/{interval}"
    return ",".join(str(value) for value in ordered)


def crons_from_simple(value: Any) -> List[str]:
    if not isinstance(value, dict):
        raise ValueError("易读计划必须是对象")
    kind = str(value.get("kind", "")).strip()
    if kind == "fixed":
        minute = parse_clock(value.get("time"), "启动时间")
        return [f"{minute % 60} {minute // 60} * * *"]
    if kind != "window":
        raise ValueError("易读计划类型必须是 fixed 或 window")

    start = parse_clock(value.get("start"), "开始时间")
    end = parse_clock(value.get("end"), "结束时间")
    try:
        interval = int(value.get("interval_minutes"))
    except (TypeError, ValueError) as exc:
        raise ValueError("启动间隔必须是分钟数") from exc
    if interval not in SIMPLE_INTERVALS:
        choices = "、".join(str(item) for item in sorted(SIMPLE_INTERVALS))
        raise ValueError(f"启动间隔只支持 {choices} 分钟")

    duration = (end - start) % (24 * 60)
    if duration == 0:
        duration = 24 * 60
    if duration % interval:
        raise ValueError("运行窗口长度必须是启动间隔的整数倍")

    slots = [(start + offset) % (24 * 60) for offset in range(0, duration, interval)]
    by_hour: Dict[int, List[int]] = {}
    for slot in slots:
        by_hour.setdefault(slot // 60, []).append(slot % 60)

    grouped_hours: Dict[tuple[int, ...], List[int]] = {}
    for hour, minutes in by_hour.items():
        grouped_hours.setdefault(tuple(sorted(minutes)), []).append(hour)
    result = [
        f"{minute_field(list(minutes))} {compress_numbers(hours)} * * *"
        for minutes, hours in sorted(grouped_hours.items(), key=lambda item: min(item[1]))
    ]
    return normalize_crons(result)


def simple_from_crons(expressions: Any) -> Optional[Dict[str, Any]]:
    try:
        normalized = normalize_crons(expressions)
    except ValueError:
        return None
    if any(expression.split()[2:] != ["*", "*", "*"] for expression in normalized):
        return None

    day_start = datetime(2026, 1, 5)
    day_end = day_start + timedelta(days=1)
    slots = set()
    for expression in normalized:
        iterator = croniter(expression, day_start - timedelta(minutes=1))
        while True:
            current = iterator.get_next(datetime)
            if current >= day_end:
                break
            slots.add(current.hour * 60 + current.minute)
    ordered = sorted(slots)
    if not ordered:
        return None
    if len(ordered) == 1:
        return {"kind": "fixed", "time": clock_text(ordered[0])}

    gaps = [
        (ordered[(index + 1) % len(ordered)] - ordered[index]) % (24 * 60)
        for index in range(len(ordered))
    ]
    interval = min(gaps)
    if interval not in SIMPLE_INTERVALS:
        return None
    large_gaps = [index for index, gap in enumerate(gaps) if gap > interval]
    if len(large_gaps) > 1 or any(gap < interval for gap in gaps):
        return None
    if any(gap != interval for gap in gaps if gap <= interval):
        return None

    if large_gaps:
        first_index = (large_gaps[0] + 1) % len(ordered)
        rotated = ordered[first_index:] + ordered[:first_index]
    else:
        rotated = ordered
    start = rotated[0]
    end = (rotated[-1] + interval) % (24 * 60)
    return {
        "kind": "window",
        "start": clock_text(start),
        "end": clock_text(end),
        "interval_minutes": interval,
    }


def describe_simple_schedule(value: Dict[str, Any]) -> str:
    if value.get("kind") == "fixed":
        return f"每天 {value['time']} 启动"
    start = str(value["start"])
    end = str(value["end"])
    interval = int(value["interval_minutes"])
    if start == end:
        window = f"每天全天（从 {start} 起）"
    elif end < start:
        window = f"每天 {start}–次日 {end}"
    else:
        window = f"每天 {start}–{end}"
    return f"{window}，每 {interval} 分钟启动"


def validate_project_schedule(value: Any) -> Dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("schedule.yaml 必须是 YAML 对象")
    timezone_name = str(value.get("timezone", "Asia/Shanghai")).strip()
    timezone_info(timezone_name)
    return {
        "version": 1,
        "timezone": timezone_name,
        "enabled": bool(value.get("enabled", True)),
        "paused": bool(value.get("paused", False)),
        "force_run": bool(value.get("force_run", False)),
        "cron": normalize_crons(value.get("cron", [])),
    }


def schedule_minute(
    schedule: Dict[str, Any],
    now: Optional[datetime] = None,
) -> str:
    current = local_now(str(schedule.get("timezone", "Asia/Shanghai")), now)
    return current.strftime("%Y-%m-%dT%H:%M%z")


def matching_crons(
    schedule: Dict[str, Any],
    now: Optional[datetime] = None,
) -> List[str]:
    normalized = validate_project_schedule(schedule)
    current = local_now(normalized["timezone"], now).replace(second=0, microsecond=0)
    return [
        expression
        for expression in normalized["cron"]
        if croniter.match(expression, current)
    ]


def project_trigger(
    schedule: Dict[str, Any],
    last_cron_minute: Optional[str],
    now: Optional[datetime] = None,
) -> Optional[Dict[str, Any]]:
    normalized = validate_project_schedule(schedule)
    if not normalized["enabled"] or normalized["paused"]:
        return None
    if normalized["force_run"]:
        return {
            "reason": "manual",
            "matched_cron": None,
            "cron_minute": None,
            "triggered_at": utc_text(now),
        }
    minute = schedule_minute(normalized, now)
    if minute == last_cron_minute:
        return None
    matches = matching_crons(normalized, now)
    if not matches:
        return None
    return {
        "reason": "cron",
        "matched_cron": matches[0],
        "cron_minute": minute,
        "triggered_at": utc_text(now),
    }


def next_project_run(
    schedule: Dict[str, Any],
    now: Optional[datetime] = None,
) -> Optional[str]:
    normalized = validate_project_schedule(schedule)
    if not normalized["enabled"] or normalized["paused"]:
        return None
    if normalized["force_run"]:
        return utc_text(now)
    current = local_now(normalized["timezone"], now)
    candidates = [
        croniter(expression, current).get_next(datetime)
        for expression in normalized["cron"]
    ]
    return utc_text(min(candidates)) if candidates else None


def schedule_view(
    schedule: Dict[str, Any],
    now: Optional[datetime] = None,
) -> Dict[str, Any]:
    normalized = validate_project_schedule(schedule)
    simple = simple_from_crons(normalized["cron"])
    description = (
        describe_simple_schedule(simple)
        if simple is not None
        else f"自定义 Cron（{len(normalized['cron'])} 条）"
    )
    return {
        "description": description,
        "simple": simple,
        "next_run_at": next_project_run(normalized, now),
    }


def next_schedule_check(now: Optional[datetime] = None) -> str:
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    current = current.astimezone(timezone.utc)
    next_minute = current.replace(second=0, microsecond=0) + timedelta(minutes=1)
    return next_minute.isoformat().replace("+00:00", "Z")
