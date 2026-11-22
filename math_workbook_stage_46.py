# === Stage 46: Настройки из окружения ===
# Project: MathWorkbook
import os
import json


PROJECT_ENV_PREFIX = "MATHWORKBOOK_"


def load_project_settings():
    settings = {}

    def _get(key):
        value = os.environ.get(key)
        if value is None:
            return None
        return value

    difficulty = _get(f"{PROJECT_ENV_PREFIX}DEFAULT_DIFFICULTY")
    if difficulty is not None:
        settings["default_difficulty"] = _coerce_difficulty(difficulty)

    topics = _get(f"{PROJECT_ENV_PREFIX}DEFAULT_TOPICS")
    if topics is not None:
        settings["default_topics"] = _parse_topics(topics)

    max_attempts = _get(f"{PROJECT_ENV_PREFIX}MAX_ATTEMPTS")
    if max_attempts is not None:
        settings["max_attempts"] = _coerce_int(max_attempts)

    auto_grade = _get(f"{PROJECT_ENV_PREFIX}AUTO_GRADE")
    if auto_grade is not None:
        settings["auto_grade"] = _coerce_bool(auto_grade)

    return settings


def _coerce_difficulty(value):
    value = value.strip().lower()
    if value in ("easy", "medium", "hard"):
        return value
    return None


def _parse_topics(value):
    cleaned = value.replace(",", " ").replace(";", " ").strip()
    if not cleaned:
        return []
    return [topic.strip().lower() for topic in cleaned.split() if topic.strip()]


def _coerce_int(value):
    try:
        number = int(value)
    except (ValueError, TypeError):
        return None
    if number <= 0:
        return None
    return number


def _coerce_bool(value):
    normalized = value.strip().lower()
    if normalized in ("1", "true", "yes", "on"):
        return True
    if normalized in ("0", "false", "no", "off", ""):
        return False
    return None


def settings_to_dict(settings):
    return {
        "default_difficulty": settings.get("default_difficulty"),
        "default_topics": settings.get("default_topics"),
        "max_attempts": settings.get("max_attempts"),
        "auto_grade": settings.get("auto_grade"),
    }


def save_settings_to_file(settings, path):
    payload = settings_to_dict(settings)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def load_settings_from_file(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)
