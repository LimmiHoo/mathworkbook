# === Stage 20: История изменений ===
# Project: MathWorkbook
from datetime import datetime


class HistoryEntry:
    def __init__(self, changed_at, description):
        self.changed_at = datetime.fromisoformat(changed_at)
        self.description = description

    def __repr__(self):
        return (
            f"HistoryEntry("
            f"changed_at={self.changed_at.isoformat()}, "
            f"description={self.description!r})"
        )


class Task:
    def __init__(self, condition, topic, difficulty, status):
        self.condition = condition
        self.topic = topic
        self.difficulty = difficulty
        self.status = status
        self.history = []

    def log_change(self, description):
        self.history.append(HistoryEntry(datetime.now().isoformat(), description))

    def get_last_change(self):
        if not self.history:
            return None
        return self.history[-1]

    def get_history(self):
        return list(self.history)

    def __repr__(self):
        return (
            f"Task("
            f"condition={self.condition!r}, "
            f"topic={self.topic!r}, "
            f"difficulty={self.difficulty!r}, "
            f"status={self.status!r}, "
            f"history_length={len(self.history)})"
        )
