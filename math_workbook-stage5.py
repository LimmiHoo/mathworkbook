# === Stage 5: Связи между сущностями ===
# Project: MathWorkbook
from collections import defaultdict


def load_attempts_from_problem(problem_id):
    """Fetch all attempts associated with a given problem.

    The function reads the attempts table and returns a list of attempt
    dictionaries, each linked to the requested problem_id.
    """
    attempts = []
    with open("attempts.csv", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            attempt_id, problem_id, user_id, value, is_correct, timestamp = (
                part for part in line.split(",")
            )
            if problem_id != problem_id:
                continue
            attempts.append(
                {
                    "attempt_id": attempt_id,
                    "problem_id": problem_id,
                    "user_id": user_id,
                    "value": value,
                    "is_correct": is_correct,
                    "timestamp": timestamp,
                }
            )
    return attempts


def check_integrity(problem_id, attempts):
    """Verify the referential integrity of the problem-attempt link.

    Ensures every returned attempt belongs to the requested problem and
    reports any anomalies found in the data.
    """
    issues = []

    if attempts is None:
        issues.append("attempts collection is empty")
        return issues

    for index, current in enumerate(attempts):
        if current.get("problem_id") != problem_id:
            issues.append(
                "attempt index {} does not match problem {}".format(
                    index, problem_id
                )
            )
        if current.get("attempt_id") in (None, "", "null"):
            issues.append("attempt {} has invalid attempt_id".format(index))
        if current.get("is_correct") not in ("true", "false"):
            issues.append("attempt {} has invalid is_correct".format(index))

    return issues


def group_attempts_by_problem(attempts):
    """Group attempts by their problem_id for quick lookups."""
    grouped = defaultdict(list)
    for current in attempts:
        grouped[current["problem_id"]].append(current)
    return grouped


def summarize_attempts(attempts):
    """Produce a basic summary of the provided attempts."""
    total = len(attempts)
    correct = 0
    for current in attempts:
        if current.get("is_correct") == "true":
            correct += 1
    return {
        "total_attempts": total,
        "correct_attempts": correct,
        "accuracy": (correct / total) if total else 0.0,
    }


def fetch_problem_attempts(problem_id):
    """Retrieve and validate all attempts for a single problem."""
    attempts = load_attempts_from_problem(problem_id)
    issues = check_integrity(problem_id, attempts)
    summary = summarize_attempts(attempts)
    if issues:
        summary["integrity_issues"] = issues
    else:
        summary["integrity_issues"] = []
    return attempts, summary
