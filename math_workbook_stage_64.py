# === Stage 64: Ближайшая неделя ===
# Project: MathWorkbook
from datetime import date, timedelta, datetime


def _parse_task_date(task):
    if isinstance(task, dict):
        raw = task.get("date")
        if isinstance(raw, str):
            return datetime.strptime(raw, "%Y-%m-%d").date()
        return raw
    return None


def group_attempts_by_day(attempts):
    grouped = {}
    for attempt in attempts or []:
        day = _parse_task_date(attempt)
        if day is None:
            continue
        key = day.strftime("%Y-%m-%d")
        grouped.setdefault(key, []).append(attempt)
    return grouped


def build_week_schedule(attempts, today=None):
    today = today or date.today()
    grouped = group_attempts_by_day(attempts)
    schedule = {}
    for offset in range(7):
        current = today + timedelta(days=offset)
        key = current.strftime("%Y-%m-%d")
        schedule[key] = grouped.get(key, [])
    return schedule


def format_schedule(schedule):
    lines = []
    for day_key, day_attempts in schedule.items():
        day = date.fromisoformat(day_key)
        weekday = day.strftime("%A")
        label = f"{day.isoformat()} ({weekday})"
        lines.append(f"{label}: {len(day_attempts)} attempt(s)")
        for attempt in day_attempts:
            task_id = attempt.get("task", {}).get("id", "unknown")
            result = attempt.get("result", "pending")
            lines.append(f"    - task {task_id} -> {result}")
    return "\n".join(lines)


def summarize_week(attempts, today=None):
    grouped = group_attempts_by_day(attempts)
    total = len(grouped)
    solved = sum(1 for attempts_list in grouped.values() for a in attempts_list if a.get("result") == "solved")
    pending = sum(1 for attempts_list in grouped.values() for a in attempts_list if a.get("result") == "pending")
    return {"total_days": total, "solved": solved, "pending": pending}


def plan_next_7_days(attempts, today=None):
    schedule = build_week_schedule(attempts, today)
    return {
        "start": schedule.get((today or date.today()).strftime("%Y-%m-%d"), []),
        "days": schedule,
        "formatted": format_schedule(schedule),
        "summary": summarize_week(attempts, today),
    }
