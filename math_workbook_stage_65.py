# === Stage 65: Тесты основных операций ===
# Project: MathWorkbook
import unittest


class Task:
    def __init__(self, statement, topic, difficulty, status):
        self.statement = statement
        self.topic = topic
        self.difficulty = difficulty
        self.status = status

    def __eq__(self, other):
        return (
            isinstance(other, Task)
            and self.statement == other.statement
            and self.topic == other.topic
            and self.difficulty == other.difficulty
            and self.status == other.status
        )

    def set_status(self, status):
        self.status = status

    def set_topic(self, topic):
        self.topic = topic

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_statement(self, statement):
        self.statement = statement


class TaskTest(unittest.TestCase):
    def test_create_task(self):
        task = Task("Solve for x", "algebra", "easy", "open")
        self.assertEqual(task.statement, "Solve for x")
        self.assertEqual(task.topic, "algebra")
        self.assertEqual(task.difficulty, "easy")
        self.assertEqual(task.status, "open")

    def test_task_equality(self):
        task1 = Task("Find roots", "equations", "medium", "open")
        task2 = Task("Find roots", "equations", "medium", "open")
        self.assertEqual(task1, task2)

    def test_task_inequality(self):
        task1 = Task("Find roots", "equations", "medium", "open")
        task2 = Task("Find roots", "equations", "hard", "open")
        self.assertNotEqual(task1, task2)

    def test_set_status(self):
        task = Task("Solve for x", "algebra", "easy", "open")
        task.set_status("solved")
        self.assertEqual(task.status, "solved")

    def test_set_topic(self):
        task = Task("Solve for x", "algebra", "easy", "open")
        task.set_topic("geometry")
        self.assertEqual(task.topic, "geometry")

    def test_set_difficulty(self):
        task = Task("Solve for x", "algebra", "easy", "open")
        task.set_difficulty("hard")
        self.assertEqual(task.difficulty, "hard")

    def test_set_statement(self):
        task = Task("Solve for x", "algebra", "easy", "open")
        task.set_statement("Solve for y")
        self.assertEqual(task.statement, "Solve for y")


if __name__ == "__main__":
    unittest.main()
