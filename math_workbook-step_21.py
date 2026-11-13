# === Stage 21: Просмотр истории ===
# Project: MathWorkbook
def format_task_history_record(record):
    """
    Render a single 'task' history record in compact form.
    Accepts a dict-like record with keys:
        'id', 'statement', 'topic', 'difficulty', 'status'
    Returns a one-line string suitable for a history view.
    """
    task_id = str(record.get('id', '?'))
    topic = str(record.get('topic', 'general')).strip()
    difficulty = str(record.get('difficulty', 'n/a')).strip()
    status = str(record.get('status', 'unknown')).strip()

    statement = str(record.get('statement', '')).strip()
    if len(statement) > 60:
        statement = statement[:57] + '...'

    return (
        f"[{task_id}] {difficulty:<5} | {topic:<12} | {status:<8} | {statement}"
    )


def format_task_history_records(records):
    """
    Render a collection of 'task' history records, each on its own line.
    Returns a single string with blank line separator between groups.
    """
    if not records:
        return "No task history available."

    lines = [format_task_history_record(record) for record in records]
    return "\n".join(lines)


def render_task_history_view(history_records, max_shown=20):
    """
    Build a compact task-history view.
    Shows up to max_shown records; indicates truncation if more exist.
    """
    total = len(history_records)
    if total == 0:
        return "Task history is empty. Start solving problems now!"

    shown = history_records[:max_shown]
    body = format_task_history_records(shown)

    if total > max_shown:
        body += f"\n\n... and {total - max_shown} more records."

    return body
