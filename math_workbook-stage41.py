# === Stage 41: Отчёт в Markdown ===
# Project: MathWorkbook
def export_report_markdown(report):
    """Export the MathWorkbook report as a Markdown table.

    Args:
        report: dict with keys 'title', 'topics' and 'attempts'.
            'topics' is a list of topic dicts, each having 'name',
            'difficulty', 'total', 'solved' and 'errors'.
            'attempts' is a list of attempt dicts, each having
            'task', 'topic', 'result' and 'timestamp'.

    Returns:
        str: Markdown-formatted report string.
    """
    lines = []
    lines.append("# " + report.get("title", "Math Workbook Report"))
    lines.append("")

    topic_rows = []
    for topic in report.get("topics", []):
        name = topic.get("name", "")
        diff = topic.get("difficulty", "")
        total = topic.get("total", 0)
        solved = topic.get("solved", 0)
        errors = topic.get("errors", 0)
        topic_rows.append(
            (name, diff, str(total), str(solved), str(errors))
        )

    lines.append("## Topics")
    lines.append("")
    lines.append("| Topic | Difficulty | Total | Solved | Errors |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in topic_rows:
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    attempt_rows = []
    for attempt in report.get("attempts", []):
        task = attempt.get("task", "")
        topic = attempt.get("topic", "")
        result = attempt.get("result", "")
        timestamp = attempt.get("timestamp", "")
        attempt_rows.append(
            (task, topic, result, timestamp)
        )

    lines.append("## Attempts")
    lines.append("")
    lines.append("| Task | Topic | Result | Timestamp |")
    lines.append("| --- | --- | --- | --- |")
    for row in attempt_rows:
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    return "\n".join(lines)
