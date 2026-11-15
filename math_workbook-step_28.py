# === Stage 28: Календарная сетка ===
# Project: MathWorkbook
import calendar
from datetime import date


class AttemptCalendar:
    """Textual grid rendering of attempts for a month."""

    def __init__(self, attempts, year, month):
        self.attempts = attempts
        self.year = year
        self.month = month

    def _index(self, attempt):
        return attempt.get("day")

    def _grid(self):
        grid = {}
        for attempt in self.attempts:
            day = self._index(attempt)
            if day is not None:
                grid[day] = grid.get(day, []) + [attempt]
        return grid

    def _render(self):
        lines = []
        lines.append(f"{calendar.month_name[self.month]} {self.year}")
        lines.append("")
        lines.append(calendar.month(self.year, self.month))
        lines.append("")
        grid = self._grid()
        for day in sorted(grid):
            count = len(grid[day])
            if count:
                attempt = grid[day][0]
                tag = attempt.get("status", "attempt")
                lines.append(f"{day:>2}  {count}  {tag}")
        return "\n".join(lines)

    def render(self):
        return self._render()


def render_attempt_calendar(attempts, year, month):
    return AttemptCalendar(attempts, year, month).render()
