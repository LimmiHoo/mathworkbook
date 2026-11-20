# === Stage 42: HTML-отчёт ===
# Project: MathWorkbook
def generate_html_report(tasks, attempts):
    """Build a standalone HTML report string from tasks and attempts.

    tasks: iterable of dicts with keys condition, topic, difficulty, status
    attempts: iterable of dicts with keys task_id, correct
    """
    def escape(value):
        if value is None:
            return ""
        return (
            str(value)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )

    def difficulty_label(difficulty):
        if difficulty in ("easy", "medium", "hard"):
            return str(difficulty)
        return "unknown"

    def status_label(status):
        if status in ("solved", "pending", "blocked"):
            return str(status)
        return "unknown"

    rows = []
    for task in tasks:
        task_id = task.get("id", "")
        condition = task.get("condition", "")
        topic = task.get("topic", "")
        difficulty = difficulty_label(task.get("difficulty", ""))
        status = status_label(task.get("status", ""))

        attempts_for_task = [
            a for a in attempts if a.get("task_id", "") == task_id
        ]
        solved = any(a.get("correct", False) for a in attempts_for_task)

        cells = [
            escape(task_id),
            escape(topic),
            escape(difficulty),
            escape(status),
            escape(condition),
            str(len(attempts_for_task)),
            "yes" if solved else "no",
        ]
        rows.append("\t".join(cells))

    rows_joined = "\n".join(rows) if rows else "No data"

    body = (
        "<html><head><meta charset='utf-8'>"
        "<title>MathWorkbook Report</title></head><body>"
        "<h1>Math Workbook Report</h1>"
        "<table border='1' cellpadding='4'>"
        "<tr><th>Task ID</th><th>Topic</th><th>Difficulty</th>"
        "<th>Status</th><th>Condition</th><th>Attempts</th><th>Solved</th></tr>"
        "<tr>" + rows_joined + "</tr>"
        "</table></body></html>"
    )
    return body


if __name__ == "__main__":
    sample_tasks = [
        {"id": "Q1", "condition": "Solve 2 + 2", "topic": "arithmetic",
         "difficulty": "easy", "status": "solved"},
        {"id": "Q2", "condition": "Solve 5 * 3", "topic": "arithmetic",
         "difficulty": "easy", "status": "pending"},
    ]
    sample_attempts = [
        {"task_id": "Q1", "correct": True},
        {"task_id": "Q2", "correct": False},
    ]
    report = generate_html_report(sample_tasks, sample_attempts)
    print(report)
