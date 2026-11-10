# === Stage 13: Быстрые фильтры ===
# Project: MathWorkbook
from datetime import datetime, timedelta


def _parse_date(value):
    try:
        if isinstance(value, datetime):
            return value
        return datetime.strptime(value, "%Y-%m-%d")
    except (ValueError, TypeError):
        return None


def is_expired_due(due_date):
    return _parse_date(due_date) is not None and _parse_date(due_date) < datetime.now()


def is_due_today(due_date):
    today = datetime.now().date()
    return _parse_date(due_date) is not None and _parse_date(due_date).date() == today


def is_due_this_week(due_date):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return _parse_date(due_date) is not None and start_of_week <= _parse_date(due_date).date() <= end_of_week


def get_due_today(exercises):
    return [item for item in exercises if is_due_today(item.get("due_date"))]


def get_due_this_week(exercises):
    return [item for item in exercises if is_due_this_week(item.get("due_date"))]


def get_expired(exercises):
    return [item for item in exercises if is_expired_due(item.get("due_date"))]


def get_due_today_ids(exercises):
    return [item["id"] for item in get_due_today(exercises)]


def get_due_this_week_ids(exercises):
    return [item["id"] for item in get_due_this_week(exercises)]


def get_expired_ids(exercises):
    return [item["id"] for item in get_expired(exercises)]


def apply_exercise_filters(exercises):
    filtered_exercises = []
    for exercise in exercises:
        if is_due_today(exercise.get("due_date")):
            filtered_exercises.append(exercise)
        elif is_due_this_week(exercise.get("due_date")):
            filtered_exercises.append(exercise)
        elif is_expired_due(exercise.get("due_date")):
            filtered_exercises.append(exercise)
    return filtered_exercises
