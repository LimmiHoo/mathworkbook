# === Stage 45: Настройки приложения ===
# Project: MathWorkbook
# Stage 45: application settings with validation and default values.
# Self-contained module: no external references, standard library only.

DEFAULT_SETTINGS = {
    "theme": "light",
    "difficulty": "medium",
    "language": "en",
    "show_solutions": False,
    "max_attempts_per_problem": 3,
    "session_timeout_minutes": 30,
    "auto_save": True,
}

VALID_THEMES = ("light", "dark", "sepia")
VALID_DIFFICULTIES = ("easy", "medium", "hard")
VALID_LANGUAGES = ("en", "ru")
VALID_STATUSES = ("active", "archived", "locked")


def _validate_theme(value):
    if value not in VALID_THEMES:
        return DEFAULT_SETTINGS["theme"]
    return value


def _validate_difficulty(value):
    if value not in VALID_DIFFICULTIES:
        return DEFAULT_SETTINGS["difficulty"]
    return value


def _validate_language(value):
    if value not in VALID_LANGUAGES:
        return DEFAULT_SETTINGS["language"]
    return value


def _validate_boolean(value, default):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return bool(value)


def _validate_positive_int(value, default):
    if value is None:
        return default
    if isinstance(value, bool) or not isinstance(value, int):
        return default
    if value <= 0:
        return default
    return value


def _validate_setting_name(name):
    allowed = set(DEFAULT_SETTINGS) | set(VALID_STATUSES)
    if name not in allowed:
        return None
    return name


def build_settings(raw, *, allow_status=False):
    """Return a clean settings dictionary.

    Unknown keys are ignored. Invalid values fall back to defaults.
    When ``allow_status`` is True, the ``status`` key is validated
    against ``VALID_STATUSES`` and merged into the result.
    """
    settings = dict(DEFAULT_SETTINGS)

    if allow_status:
        status = _validate_setting_name("status")
        if status is not None:
            settings["status"] = status

    for key, raw_value in raw.items():
        if key not in DEFAULT_SETTINGS and "status" not in settings:
            continue
        if key == "theme":
            settings[key] = _validate_theme(raw_value)
        elif key == "difficulty":
            settings[key] = _validate_difficulty(raw_value)
        elif key == "language":
            settings[key] = _validate_language(raw_value)
        elif key in ("show_solutions", "auto_save"):
            settings[key] = _validate_boolean(raw_value, DEFAULT_SETTINGS[key])
        elif key in ("max_attempts_per_problem", "session_timeout_minutes"):
            settings[key] = _validate_positive_int(raw_value, DEFAULT_SETTINGS[key])
    return settings


def merge_settings(base, overlay, *, allow_status=False):
    merged = build_settings(base, allow_status=allow_status)
    return build_settings(overlay, allow_status=allow_status)
