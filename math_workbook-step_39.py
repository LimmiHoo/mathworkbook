# === Stage 39: Загрузка из файла ===
# Project: MathWorkbook
def load_state(path, default):
    """Load saved workbook state from a JSON file.

    Returns the deserialized state dict. Falls back to the provided default
    when the file is missing or its contents cannot be parsed.
    """
    if not path:
        return default

    try:
        with open(path, "r", encoding="utf-8") as handle:
            raw = handle.read()
    except FileNotFoundError:
        return default
    except OSError as error:
        print("Could not read state file:", error)
        return default

    try:
        return json.loads(raw)
    except json.JSONDecodeError as error:
        print("State file is corrupted, ignoring:", error)
        return default
