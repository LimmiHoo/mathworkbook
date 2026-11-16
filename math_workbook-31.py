# === Stage 31: Активность по дням недели ===
# Project: MathWorkbook
import calendar
from collections import defaultdict
from datetime import datetime


WEEKDAY_LABELS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def _load_attempts(tasks):
    stats = defaultdict(list)
    for task in tasks:
        for attempt in task.attempts:
            stats[attempt.day].append(attempt)
    return stats


def render_activity_map(tasks, reference_date=None):
    stats = _load_attempts(tasks)
    start_index = 0
    if reference_date is not None:
        start_index = reference_date.weekday()
    lines = []
    lines.append("Activity by Day")
    lines.append("Day: solved / total / avg")
    for offset, label in enumerate(WEEKDAY_LABELS):
        index = (start_index + offset) % 7
        attempts = stats.get(index, [])
        solved = sum(1 for a in attempts if a.status == "solved")
        total = len(attempts)
        average = (solved / total) if total else 0.0
        lines.append(f"{label}: {solved} / {total} / {average:.2f}")
    return "\n".join(lines)


def activity_map(tasks, reference_date=None):
    return render_activity_map(tasks, reference_date)


if __name__ == "__main__":
    sample_tasks = [
        {
            "id": "task-1",
            "statement": "Solve 2x + 5 = 15",
            "topic": "algebra",
            "difficulty": "easy",
            "attempts": [
                {"day": 0, "status": "solved", "points": 10},
                {"day": 3, "status": "solved", "points": 10},
                {"day": 5, "status": "failed", "points": 0},
            ],
        },
        {
            "id": "task-2",
            "statement": "Compute 7 * 8",
            "topic": "arithmetic",
            "difficulty": "easy",
            "attempts": [
                {"day": 1, "status": "solved", "points": 5},
                {"day": 2, "status": "failed", "points": 0},
            ],
        },
    ]
    print(activity_map(sample_tasks))
