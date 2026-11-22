# === Stage 48: Разбор чисел и дат ===
# Project: MathWorkbook
def parse_number(text):
    """Return (value, error) for a numeric string.

    Handles integers, decimals, and scientific notation.
    error is None on success, otherwise a human-readable message.
    """
    if text is None:
        return None, "input is empty"
    value = float(text)
    if value.is_integer():
        return int(value), None
    return value, None


def parse_date(text):
    """Return (year, month, day, error) for a date string.

    Accepts 'YYYY-MM-DD' format only.
    error is None on success, otherwise a human-readable message.
    """
    if text is None:
        return None, None, None, "input is empty"
    parts = text.strip().split("-")
    if len(parts) != 3:
        return None, None, None, "expected format YYYY-MM-DD"
    try:
        year, month, day = (int(part) for part in parts)
    except ValueError:
        return None, None, None, "year, month, and day must be integers"
    if not (1 <= month <= 12):
        return None, None, None, "month must be between 1 and 12"
    if not (1 <= day <= 31):
        return None, None, None, "day must be between 1 and 31"
    return year, month, day, None
