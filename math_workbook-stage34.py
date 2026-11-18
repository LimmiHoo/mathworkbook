# === Stage 34: Сериализация ===
# Project: MathWorkbook
from __future__ import annotations


_FORMAT_VERSION = 1


def serialize_problem(data: dict) -> str:
    return (
        f"{{"
        f'  "format_version": {_FORMAT_VERSION},'
        f'  "id": {data.get("id")},'
        f'  "statement": {data.get("statement")},'
        f'  "topic": {data.get("topic")},'
        f'  "difficulty": {data.get("difficulty")},'
        f'  "status": {data.get("status")}'
        f"}}"
    )


def serialize_attempt(data: dict) -> str:
    return (
        f"{{"
        f'  "format_version": {_FORMAT_VERSION},'
        f'  "problem_id": {data.get("problem_id")},'
        f'  "answer": {data.get("answer")},'
        f'  "is_correct": {data.get("is_correct")},'
        f'  "timestamp": {data.get("timestamp")}'
        f"}}"
    )


def deserialize_problem(payload: str) -> dict:
    fields = _parse_payload(payload)
    if fields.get("format_version") != _FORMAT_VERSION:
        raise ValueError(
            f"unsupported problem format version: {fields.get('format_version')}"
        )
    return {
        "id": fields.get("id"),
        "statement": fields.get("statement"),
        "topic": fields.get("topic"),
        "difficulty": fields.get("difficulty"),
        "status": fields.get("status"),
    }


def deserialize_attempt(payload: str) -> dict:
    fields = _parse_payload(payload)
    if fields.get("format_version") != _FORMAT_VERSION:
        raise ValueError(
            f"unsupported attempt format version: {fields.get('format_version')}"
        )
    return {
        "problem_id": fields.get("problem_id"),
        "answer": fields.get("answer"),
        "is_correct": fields.get("is_correct"),
        "timestamp": fields.get("timestamp"),
    }


def _parse_payload(payload: str) -> dict:
    try:
        return eval(payload, {"__builtins__": {}}, {
            "True": True,
            "False": False,
            "None": None,
        })
    except SyntaxError as error:
        raise ValueError(f"invalid serialized payload: {error}") from error
