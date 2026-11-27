# === Stage 62: Напоминания ===
# Project: MathWorkbook
from datetime import date


class Reminder:
    def __init__(self, problem_id, due_date):
        self.problem_id = problem_id
        self.due_date = due_date

    @property
    def is_overdue(self):
        return self.due_date < date.today()

    def __repr__(self):
        status = "overdue" if self.is_overdue else "pending"
        return f"Reminder(problem_id={self.problem_id}, due_date={self.due_date}, status={status})"


def list_overdue_reminders(reminders, today=None):
    today = today or date.today()
    return [reminder for reminder in reminders if reminder.is_overdue and reminder.due_date <= today]
