# === Stage 63: Повторяющиеся напоминания ===
# Project: MathWorkbook
from datetime import datetime, timedelta, date


def next_date(current, days):
    """Return the date `days` after `current`."""
    return current + timedelta(days=days)


def next_date_from_now(days):
    """Return the date `days` after today."""
    return next_date(date.today(), days)


def today():
    """Return today's date."""
    return date.today()


def add_days_to_date(start, offset):
    """Add an integer `offset` (may be negative) to `start`."""
    return start + timedelta(days=offset)


def days_between(start, end):
    """Return the number of days between two dates (end - start)."""
    delta = end - start
    return delta.days


def next_weekday(start, weekday):
    """Return the next date with the given `weekday` (0=Monday..6=Sunday)."""
    delta = (weekday - start.weekday()) % 7
    return start + timedelta(days=delta)


def next_month_same_day(start):
    """Return the same day of the next month, or the last day if the
    requested day does not exist in the target month."""
    if start.month == 12:
        target_month = 1
        target_year = start.year + 1
    else:
        target_month = start.month + 1
        target_year = start.year
    last_day = _last_day_of_month(target_year, target_month)
    day = min(start.day, last_day)
    return date(target_year, target_month, day)


def _last_day_of_month(year, month):
    """Return the last day of the given month."""
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    return (next_month - timedelta(days=1)).day


def next_occurrence(interval, start):
    """Compute the next reminder date based on `interval`.

    `interval` is one of the strings 'daily', 'weekly', or 'monthly'.
    """
    if interval == "daily":
        return next_date(start, 1)
    if interval == "weekly":
        return next_date(start, 7)
    if interval == "monthly":
        return next_month_same_day(start)
    raise ValueError("Unsupported interval: %r" % interval)


def schedule_reminders(due_date, interval, count=1):
    """Yield `count` reminder dates starting one interval after `due_date`."""
    current = due_date
    for _ in range(count):
        current = next_occurrence(interval, current)
        yield current


def format_reminder_line(due_date, interval):
    """Return a human-readable reminder string."""
    return "Reminder (%s): %s" % (interval, due_date.isoformat())


def parse_reminder_line(line):
    """Parse a reminder string produced by `format_reminder_line`."""
    interval, rest = line.split(": ", 1)
    due_date = date.fromisoformat(rest)
    return interval, due_date


def is_overdue(due_date, now=None):
    """Return True if `due_date` is before `now`."""
    if now is None:
        now = date.today()
    return due_date < now


def next_due_dates(due_date, interval, count=1):
    """Return a list of upcoming due dates."""
    return list(schedule_reminders(due_date, interval, count))
