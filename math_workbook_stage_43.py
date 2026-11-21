# === Stage 43: Карточка записи ===
# Project: MathWorkbook
def render_task_card(task, max_attempts=3):
    """Render a compact card for a single task with nested attempts."""
    lines = []
    lines.append("=" * 40)
    lines.append(f"Task: {task['condition']}")
    lines.append("-" * 40)
    lines.append(f"topic:  {task['topic']}")
    lines.append(f"level:  {'*' * task['difficulty']}")
    lines.append(f"status: {task['status'].upper()}")
    lines.append("=" * 40)
    attempts = task.get("attempts", [])
    if not attempts:
        lines.append("attempts: (none yet)")
    else:
        for i in range(max(1, min(max_attempts, len(attempts)))):
            attempt = attempts[i]
            lines.append(f"  [{i + 1}] result: {attempt['result']}")
            if "feedback" in attempt:
                lines.append(f"       note: {attempt['feedback']}")
    lines.append("=" * 40)
    return "\n".join(lines)
