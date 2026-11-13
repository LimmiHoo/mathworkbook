# === Stage 22: Недельный отчёт ===
# Project: MathWorkbook
def generate_weekly_report(assignment, attempts, start_date):
    """Build a weekly progress report for an assignment as a text table.

    Parameters:
        assignment (dict): fields 'title', 'topic', 'difficulty', 'status'
        attempts (list of dict): each with 'date' (YYYY-MM-DD) and 'correct' (bool)
        start_date (str): report window start, format YYYY-MM-DD

    Returns:
        str: aligned text table with a header and rows.
    """
    from datetime import datetime

    def parse_date(value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def clamp(value, low, high):
        return max(low, min(high, value))

    days_count = 7
    week_end = start_date + timedelta(days=days_count - 1)

    correct_flags = [attempt["correct"] for attempt in attempts]
    total_attempts = len(attempts)
    solved_count = sum(1 for flag in correct_flags if flag)
    accuracy = solved_count / total_attempts if total_attempts else 0.0

    difficulty_label = {
        "easy": "Easy",
        "medium": "Medium",
        "hard": "Hard",
    }.get(assignment.get("difficulty", ""), assignment.get("difficulty", ""))

    status_label = {
        "done": "Done",
        "in_progress": "In Progress",
        "pending": "Pending",
    }.get(assignment.get("status", ""), assignment.get("status", ""))

    header = (
        f"{'Date':<12}{'Result':<10}{'Topic':<12}{'Difficulty':<10}"
        f"{'Status':<12}{'Accuracy':>8}"
    )
    separator = "-" * len(header)

    lines = [header, separator]

    for day in range(days_count):
        current_day = start_date + timedelta(days=day)
        date_text = current_day.strftime("%Y-%m-%d")
        result_text = "Solved" if solved_count > 0 else "Attempt"
        accuracy_text = f"{accuracy * 100:.1f}%"
        row = (
            f"{date_text:<12}{result_text:<10}{assignment.get('topic', ''):<12}"
            f"{difficulty_label:<10}{status_label:<12}{accuracy_text:>8}"
        )
        lines.append(row)

    lines.append(separator)
    summary = (
        f"Assignment: {assignment.get('title', '')} | "
        f"Total attempts: {total_attempts} | "
        f"Solved: {solved_count} | "
        f"Report window: {start_date.strftime('%Y-%m-%d')} to "
        f"{week_end.strftime('%Y-%m-%d')}"
    )
    lines.append(summary)

    return "\n".join(lines)
