# === Stage 14: Поиск дубликатов ===
# Project: MathWorkbook
from typing import Iterable, Dict, Any, List, Hashable


def _normalize_value(raw: Any) -> Hashable:
    if raw is None:
        return ""
    text = str(raw).strip().lower()
    if not text:
        return ""
    for sign in ("-", "+"):
        if text.startswith(sign):
            text = text[1:]
    text = text.replace(",", ".").replace(" ", "")
    return text


def _normalize_condition(text: str) -> str:
    if not text:
        return ""
    cleaned = text.strip()
    cleaned = cleaned.replace("(", " ( ").replace(")", " ) ").replace(",", " , ")
    cleaned = cleaned.replace("−", "-").replace("·", "*").replace("×", "*")
    cleaned = cleaned.replace("÷", "/").replace("√", "**0.5")
    cleaned = cleaned.replace("∞", "inf").replace("≈", "=").replace("≠", "!=")
    cleaned = cleaned.replace("≤", "<=").replace("≥", ">=").replace("±", "")
    cleaned = cleaned.replace("...", "...").replace("…", "...")
    cleaned = " ".join(cleaned.split())
    return cleaned


def normalize_task(task: Dict[str, Any]) -> Dict[str, Hashable]:
    condition = _normalize_condition(task.get("condition", ""))
    topic = _normalize_value(task.get("topic", ""))
    difficulty = _normalize_value(task.get("difficulty", ""))
    return {
        "condition": condition,
        "topic": topic,
        "difficulty": difficulty,
    }


def find_duplicate_tasks(tasks: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    normalized: Dict[Hashable, List[Dict[str, Any]]] = {}
    for task in tasks:
        signature = normalize_task(task)
        existing = normalized.setdefault(signature, [])
        if not existing:
            existing.append(task)
        else:
            if existing[0].get("id") != task.get("id"):
                existing.append(task)
    duplicates = [group for group in normalized.values() if len(group) > 1]
    duplicates.sort(key=lambda group: len(group), reverse=True)
    return [task for group in duplicates for task in group]
