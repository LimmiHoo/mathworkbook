# === Stage 19: Смена статуса ===
# Project: MathWorkbook
def _valid_transitions():
    """Return the set of statuses a task may transition into from any status."""
    return {"solved", "aborted", "pending"}


def _is_transition_allowed(current_status, next_status):
    """Return True if moving from current_status to next_status is permitted.

    Pending tasks may move anywhere. Solved tasks may only become aborted.
    Aborted tasks may only become pending.
    """
    if current_status == "pending":
        return next_status in _valid_transitions()
    if current_status == "solved":
        return next_status == "aborted"
    if current_status == "aborted":
        return next_status == "pending"
    return False


def change_task_status(task, next_status, reason):
    """Change a task's status, validating the move and recording the reason.

    Returns a new task dict with updated status and reason. Raises ValueError
    if the transition is not allowed or reason is missing.
    """
    if not reason:
        raise ValueError("reason must be a non-empty string")

    if not _is_transition_allowed(task["status"], next_status):
        raise ValueError(
            f"invalid transition from {task['status']} to {next_status}"
        )

    return {
        "id": task["id"],
        "statement": task["statement"],
        "topic": task["topic"],
        "difficulty": task["difficulty"],
        "status": next_status,
        "reason": reason,
        "attempts": task.get("attempts", []),
    }
