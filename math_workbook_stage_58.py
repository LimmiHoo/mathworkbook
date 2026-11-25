# === Stage 58: Шаблоны записей ===
# Project: MathWorkbook
from dataclasses import dataclass, field, replace


@dataclass
class Task:
    """A single math exercise with its metadata."""

    statement: str
    topic: str
    difficulty: str
    status: str = "unattempted"


@dataclass
class Attempt:
    """One try at solving a task."""

    task_id: str
    correct: bool
    notes: str = ""


def build_task(
    statement: str,
    topic: str,
    difficulty: str,
    status: str = "unattempted",
) -> Task:
    """Create a Task from explicit fields."""
    return Task(
        statement=statement,
        topic=topic,
        difficulty=difficulty,
        status=status,
    )


def build_task_from_template(
    base: Task,
    *,
    statement: str | None = None,
    topic: str | None = None,
    difficulty: str | None = None,
    status: str | None = None,
) -> Task:
    """Create a new Task reusing most fields of a template."""
    return replace(
        base,
        statement=statement if statement is not None else base.statement,
        topic=topic if topic is not None else base.topic,
        difficulty=difficulty if difficulty is not None else base.difficulty,
        status=status if status is not None else base.status,
    )
