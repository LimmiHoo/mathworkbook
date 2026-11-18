# === Stage 35: Экспорт в JSON ===
# Project: MathWorkbook
import json


def build_problem_dict(problem):
    problem_dict = {
        "condition": problem["condition"],
        "topic": problem["topic"],
        "difficulty": problem["difficulty"],
        "status": problem["status"],
    }
    return problem_dict


def build_attempt_dict(attempt, problem):
    attempt_dict = {
        "problem_id": problem["id"],
        "answer": attempt["answer"],
        "expected_answer": problem["expected_answer"],
        "is_correct": attempt["is_correct"],
        "timestamp": attempt["timestamp"],
    }
    return attempt_dict


def export_workbook_to_json(workbook):
    problems = [build_problem_dict(problem) for problem in workbook["problems"]]
    problems.sort(key=lambda problem: (problem["topic"], problem["difficulty"], problem["id"]))

    attempts = [build_attempt_dict(attempt, problem) for attempt in workbook["attempts"]]
    attempts.sort(key=lambda attempt: (attempt["problem_id"], attempt["timestamp"]))

    exported = {
        "metadata": {
            "title": workbook["title"],
            "version": workbook["version"],
            "problem_count": len(problems),
            "attempt_count": len(attempts),
        },
        "problems": problems,
        "attempts": attempts,
    }
    return json.dumps(exported, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    sample_workbook = {
        "title": "Math Workbook",
        "version": "1.0",
        "problems": [
            {
                "id": 2,
                "condition": "Solve for x: 2x + 3 = 11",
                "topic": "Linear Equations",
                "difficulty": "easy",
                "status": "active",
                "expected_answer": 4,
            },
            {
                "id": 1,
                "condition": "Find the area of a circle with radius 5",
                "topic": "Geometry",
                "difficulty": "medium",
                "status": "active",
                "expected_answer": 78.54,
            },
        ],
        "attempts": [
            {
                "answer": 4,
                "is_correct": True,
                "timestamp": 1700000020,
            },
            {
                "answer": 78.54,
                "is_correct": True,
                "timestamp": 1700000010,
            },
        ],
    }

    exported_json = export_workbook_to_json(sample_workbook)
    print(exported_json)
