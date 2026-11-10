# === Stage 15: Слияние записей ===
# Project: MathWorkbook
def merge_attempts_with_winner(record_a, record_b):
    """Combine two task records, choosing the winner field-by-field."""
    if not isinstance(record_a, dict) or not isinstance(record_b, dict):
        raise TypeError("Both records must be dictionaries")

    merged = {}

    for field in ("statement", "topic", "difficulty", "status"):
        if field in record_a and field in record_b:
            if isinstance(record_a[field], (int, float)) and isinstance(record_b[field], (int, float)):
                winner = record_a[field] if record_a[field] >= record_b[field] else record_b[field]
            else:
                winner = record_a[field]
            merged[field] = winner
        elif field in record_a:
            merged[field] = record_a[field]
        elif field in record_b:
            merged[field] = record_b[field]
        else:
            merged[field] = None

    return merged


def merge_records(records):
    """Merge a list of task records, choosing the winner field-by-field."""
    if not records:
        return {}
    if not all(isinstance(record, dict) for record in records):
        raise TypeError("All records must be dictionaries")

    merged = {}
    for field in ("statement", "topic", "difficulty", "status"):
        values = [record.get(field) for record in records if field in record]
        if values:
            if len(values) == 1:
                merged[field] = values[0]
                continue
            if all(isinstance(value, (int, float)) for value in values):
                merged[field] = max(values)
            else:
                merged[field] = values[0]
        else:
            merged[field] = None

    return merged


if __name__ == "__main__":
    record_a = {
        "statement": "Solve for x in 2x + 3 = 11",
        "topic": "Linear equations",
        "difficulty": 3,
        "status": "pending",
    }
    record_b = {
        "statement": "Solve for x in 3x - 6 = 9",
        "topic": "Linear equations",
        "difficulty": 4,
        "status": "attempted",
    }
    merged = merge_attempts_with_winner(record_a, record_b)
    print(merged)

    combined = merge_records([record_a, record_b])
    print(combined)
