# === Stage 4: Связанная сущность ===
# Project: MathWorkbook
"""MathWorkbook attempt module: records a student attempt against an existing task."""


class Attempt:
    """A single attempt by a student on a task.

    Attributes:
        task_id: identifier of the task being attempted.
        correct: whether the attempt produced the correct answer.
        timestamp: ISO-8601 string of when the attempt was recorded.
    """

    def __init__(self, task_id, correct, timestamp):
        if not task_id:
            raise ValueError("task_id must be a non-empty string")
        if not isinstance(correct, bool):
            raise TypeError("correct must be a boolean")
        self.task_id = task_id
        self.correct = correct
        self.timestamp = timestamp

    def __repr__(self):
        status = "correct" if self.correct else "incorrect"
        return f"Attempt(task_id={self.task_id!r}, correct={status}, timestamp={self.timestamp!r})"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "correct": self.correct,
            "timestamp": self.timestamp,
        }


def add_attempt(task_id, correct, timestamp):
    """Create and return a new Attempt linked to the given task.

    Args:
        task_id: identifier of the target task.
        correct: boolean indicating if the attempt was correct.
        timestamp: ISO-8601 string recording when the attempt happened.

    Returns:
        An Attempt instance.
    """
    return Attempt(task_id, correct, timestamp)


def format_attempt_summary(attempt):
    """Return a human-readable one-line summary of an attempt."""
    return (
        f"Attempt #{attempt.task_id} on task {attempt.task_id}: "
        f"{attempt.correct} at {attempt.timestamp}."
    )
