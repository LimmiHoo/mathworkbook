# === Stage 29: Ключевые метрики ===
# Project: MathWorkbook
from collections import Counter

def calculate_project_metrics(tasks, attempts):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t.get("status") == "solved")
    solved_ratio = completed_tasks / total_tasks if total_tasks else 0.0

    topic_counter = Counter(task.get("topic", "unknown") for task in tasks)
    difficulty_counter = Counter(task.get("difficulty", "unknown") for task in tasks)
    status_counter = Counter(task.get("status", "unknown") for task in tasks)

    if attempts:
        solved_attempts = sum(1 for a in attempts if a.get("solved", False))
        success_ratio = solved_attempts / len(attempts)
        attempts_per_task = len(attempts) / total_tasks if total_tasks else 0.0
        total_attempts = len(attempts)
        failed_attempts = total_attempts - solved_attempts
    else:
        solved_attempts = 0
        success_ratio = 0.0
        attempts_per_task = 0.0
        total_attempts = 0
        failed_attempts = 0

    metrics = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "solved_ratio": round(solved_ratio, 3),
        "total_attempts": total_attempts,
        "solved_attempts": solved_attempts,
        "failed_attempts": failed_attempts,
        "success_ratio": round(success_ratio, 3),
        "attempts_per_task": round(attempts_per_task, 2),
        "topics": dict(topic_counter),
        "difficulties": dict(difficulty_counter),
        "statuses": dict(status_counter),
    }
    return metrics


def format_metrics_report(metrics):
    lines = ["Math Workbook Project Report", "=" * 32, ""]

    lines.append("Core indicators")
    lines.append(f"  Tasks: {metrics['total_tasks']} (completed: {metrics['completed_tasks']})")
    lines.append(f"  Solved ratio: {metrics['solved_ratio'] * 100:.1f}%")
    lines.append("")

    lines.append("Attempts")
    lines.append(f"  Total: {metrics['total_attempts']}")
    lines.append(f"  Solved: {metrics['solved_attempts']}")
    lines.append(f"  Failed: {metrics['failed_attempts']}")
    lines.append(f"  Success ratio: {metrics['success_ratio'] * 100:.1f}%")
    lines.append(f"  Attempts per task: {metrics['attempts_per_task']}")
    lines.append("")

    lines.append("Task distribution")
    lines.append("  Topics:")
    for topic, count in metrics["topics"].most_common():
        lines.append(f"    - {topic}: {count}")
    lines.append("  Difficulties:")
    for difficulty, count in metrics["difficulties"].most_common():
        lines.append(f"    - {difficulty}: {count}")
    lines.append("  Statuses:")
    for status, count in metrics["statuses"].most_common():
        lines.append(f"    - {status}: {count}")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    sample_tasks = [
        {"condition": "solve x", "topic": "algebra", "difficulty": "easy", "status": "solved"},
        {"condition": "integrate f", "topic": "calculus", "difficulty": "hard", "status": "pending"},
        {"condition": "solve x", "topic": "algebra", "difficulty": "medium", "status": "solved"},
    ]
    sample_attempts = [
        {"task_id": 0, "solved": True},
        {"task_id": 1, "solved": False},
        {"task_id": 2, "solved": True},
    ]

    metrics = calculate_project_metrics(sample_tasks, sample_attempts)
    print(format_metrics_report(metrics))
