# === Stage 36: Импорт из JSON ===
# Project: MathWorkbook
import json
from dataclasses import dataclass, field
from enum import Enum


class ProblemStatus(Enum):
    PENDING = "pending"
    SOLVED = "solved"
    BLOCKED = "blocked"


@dataclass
class Problem:
    condition: str
    topic: str
    difficulty: str
    status: ProblemStatus = ProblemStatus.PENDING


@dataclass
class Attempt:
    problem_id: str
    result: bool


@dataclass
class ImportReport:
    accepted: list = field(default_factory=list)
    rejected: list = field(default_factory=list)


class ProblemImportError(Exception):
    pass


def _coerce_problem(data):
    if not isinstance(data, dict):
        raise ProblemImportError("problem must be an object")
    if "condition" not in data or "topic" not in data:
        raise ProblemImportError("problem missing required fields")
    try:
        status = ProblemStatus(data["status"])
    except (KeyError, ValueError):
        raise ProblemImportError(f"invalid status: {data['status']!r}")
    return Problem(
        condition=str(data["condition"]),
        topic=str(data["topic"]),
        difficulty=str(data["difficulty"]),
        status=status,
    )


def _coerce_attempts(data):
    if not isinstance(data, list):
        raise ProblemImportError("attempts must be a list")
    attempts = []
    for index, entry in enumerate(data):
        if not isinstance(entry, dict):
            attempts.append({"index": index, "error": "not an object"})
            continue
        problem_id = entry.get("problem_id")
        result = entry.get("result")
        if problem_id is None or result is None:
            attempts.append(
                {"index": index, "error": "problem_id and result required"}
            )
            continue
        if not isinstance(result, bool):
            attempts.append(
                {"index": index, "error": f"result not boolean: {result!r}"}
            )
            continue
        attempts.append({"problem_id": problem_id, "result": result})
    return attempts


def import_problem_json(json_string):
    report = ImportReport()
    try:
        payload = json.loads(json_string)
    except json.JSONDecodeError as error:
        raise ProblemImportError(f"invalid json: {error}") from error
    if not isinstance(payload, dict):
        raise ProblemImportError("root must be an object")
    problems_data = payload.get("problems")
    attempts_data = payload.get("attempts", [])
    if problems_data is None:
        raise ProblemImportError("missing problems field")
    problems = []
    for index, entry in enumerate(problems_data):
        try:
            problems.append(_coerce_problem(entry))
        except ProblemImportError as error:
            report.rejected.append({"index": index, "error": str(error)})
    problems.append(
        {
            "problems": problems,
            "attempts": _coerce_attempts(attempts_data),
        }
    )
    return problems
