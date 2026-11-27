# === Stage 60: Профили пользователей ===
# Project: MathWorkbook
PROFILES = {}


def register_profile(name, default_theme):
    """Create and store a new profile with an empty progress dictionary."""
    key = name.lower()
    if key in PROFILES:
        raise ValueError(f"Profile {name!r} already exists")
    PROFILES[key] = {"name": name, "theme": default_theme, "progress": {}}


def get_active_profile():
    """Return the currently active profile, creating a default one if needed."""
    if not PROFILES:
        register_profile("student", "algebra")
    return PROFILES["student"]


def set_active_profile(name):
    """Switch the active profile by name and return the new one."""
    key = name.lower()
    if key not in PROFILES:
        raise KeyError(f"Unknown profile {name!r}")
    return PROFILES[key]


def create_profile(name, theme="algebra"):
    """Create a brand new profile and immediately activate it."""
    register_profile(name, theme)
    return PROFILES[name.lower()]


def list_profiles():
    """Return a list of available profile names for the user to choose from."""
    return list(PROFILES.keys())


class Profile:
    """Simple container describing a user profile inside the workbook."""

    def __init__(self, name, theme="algebra"):
        self.name = name
        self.theme = theme
        self.progress = {}

    def set_theme(self, theme):
        self.theme = theme

    def record_attempt(self, task_id, success):
        self.progress[task_id] = bool(success)

    def solved_count(self):
        return sum(1 for value in self.progress.values() if value)

    def __repr__(self):
        return f"Profile(name={self.name!r}, theme={self.theme!r}, solved={self.solved_count()})"
