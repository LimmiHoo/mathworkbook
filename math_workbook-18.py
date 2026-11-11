# === Stage 18: Статусы записей ===
# Project: MathWorkbook
from enum import Enum, auto


class TaskStatus(Enum):
    """Lifecycle statuses for a math task.

    A task moves through these states as it is created, attempted,
    solved, reviewed, and eventually archived.
    """

    DRAFT = auto()
    ACTIVE = auto()
    SOLVED = auto()
    REVIEW = auto()
    ARCHIVED = auto()

    def __str__(self) -> str:
        return self.name


def allowed_transitions(statuses: frozenset[TaskStatus]) -> frozenset[tuple[TaskStatus, TaskStatus]]:
    """Return the set of valid transitions between the given statuses.

    The transitions represent the lifecycle of a task. Each pair is an
    ordered (from, to) tuple indicating a permitted move.
    """

    transitions: frozenset[tuple[TaskStatus, TaskStatus]] = frozenset({
        (TaskStatus.DRAFT, TaskStatus.ACTIVE),
        (TaskStatus.DRAFT, TaskStatus.ARCHIVED),
        (TaskStatus.ACTIVE, TaskStatus.SOLVED),
        (TaskStatus.ACTIVE, TaskStatus.REVIEW),
        (TaskStatus.ACTIVE, TaskStatus.ARCHIVED),
        (TaskStatus.SOLVED, TaskStatus.REVIEW),
        (TaskStatus.REVIEW, TaskStatus.ACTIVE),
        (TaskStatus.REVIEW, TaskStatus.SOLVED),
        (TaskStatus.REVIEW, TaskStatus.ARCHIVED),
        (TaskStatus.SOLVED, TaskStatus.ARCHIVED),
    })
    return transitions


def is_valid_transition(from_status: TaskStatus, to_status: TaskStatus) -> bool:
    """Check whether a move from one status to another is permitted."""

    return (from_status, to_status) in allowed_transitions(frozenset({from_status, to_status}))


def reachable_statuses(start_status: TaskStatus, steps: int = 1) -> list[TaskStatus]:
    """Return statuses reachable from start_status within the given number of steps.

    Uses breadth-first traversal over the allowed transition graph.
    """

    from collections import deque

    visited: set[TaskStatus] = set()
    queue: deque[tuple[TaskStatus, int]] = deque([(start_status, 0)])

    while queue:
        current, depth = queue.popleft()

        if depth < steps:
            for next_status in allowed_transitions(frozenset({current})).__iter__():
                if next_status not in visited:
                    visited.add(next_status)
                    queue.append((next_status, depth + 1))

    return sorted(visited, key=lambda status: status.value)
