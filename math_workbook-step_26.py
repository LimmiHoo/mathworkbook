# === Stage 26: Сравнение периодов ===
# Project: MathWorkbook
def compare_periods(periods, key="score"):
    """Compare two periods by key indicators and return a comparison report."""
    if len(periods) < 2:
        raise ValueError("compare_periods needs at least two periods")

    first, second = periods[0], periods[1]

    def as_dict(period):
        return {name: period.get(name) for name in period}

    first_data = as_dict(first)
    second_data = as_dict(second)

    common_keys = sorted(set(first_data) & set(second_data))

    differences = {}
    for name in common_keys:
        first_value = first_data[name]
        second_value = second_data[name]
        try:
            delta = float(second_value) - float(first_value)
        except (TypeError, ValueError):
            delta = None
        differences[name] = {
            "first": first_value,
            "second": second_value,
            "delta": delta,
        }

    if key in differences:
        delta = differences[key]["delta"]
        if delta > 0:
            trend = "up"
        elif delta < 0:
            trend = "down"
        else:
            trend = "flat"
    else:
        trend = "unknown"

    return {
        "first": first,
        "second": second,
        "key": key,
        "trend": trend,
        "differences": differences,
    }


def compare_periods_summary(periods, key="score"):
    """Return a short human-readable summary comparing two periods."""
    result = compare_periods(periods, key=key)
    first, second = result["first"], result["second"]
    trend = result["trend"]
    line = f"{first} vs {second}: key '{key}' {trend}"
    if trend == "up":
        line += " (improved)"
    elif trend == "down":
        line += " (regressed)"
    return line


if __name__ == "__main__":
    period_a = {"topic": "algebra", "score": 8, "errors": 3}
    period_b = {"topic": "algebra", "score": 10, "errors": 1}
    print(compare_periods_summary([period_a, period_b], key="score"))
    print(compare_periods_summary([period_a, period_b], key="errors"))
