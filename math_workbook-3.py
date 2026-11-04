# === Stage 3: Хранилище в памяти ===
# Project: MathWorkbook
"""In-memory store for math problems: add, get by id, list."""


class Problem:
    def __init__(self, condition, topic, difficulty, status):
        self.condition = condition
        self.topic = topic
        self.difficulty = difficulty
        self.status = status


class ProblemStore:
    def __init__(self):
        self._problems = {}

    def add(self, problem):
        self._problems[problem.condition] = problem

    def get(self, condition):
        return self._problems.get(condition)

    def list(self):
        return list(self._problems.values())
