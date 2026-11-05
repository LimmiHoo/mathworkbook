# === Stage 8: Сортировка записей ===
# Project: MathWorkbook
from datetime import datetime


def _parse_condition(condition):
    return condition.strip().lower()


def sort_tasks_by_condition(tasks, descending=False):
    """Sort records by condition text, then by creation date (ascending).

    Ties on condition are broken by the datetime created, oldest first.
    The input list is not mutated; a new list is returned.
    """
    if descending:
        return sorted(
            tasks,
            key=lambda task: (
                _parse_condition(task.get("condition", "")),
                task.get("created", datetime.max),
            ),
            reverse=True,
        )

    def sort_key(task):
        condition = _parse_condition(task.get("condition", ""))
        created = task.get("created", datetime.max)
        return (condition, created)

    return sorted(tasks, key=sort_key)
