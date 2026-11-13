# === Stage 23: Аномальные значения ===
# Project: MathWorkbook
from typing import Iterable, List, Optional


def _median(values: List[float]) -> float:
    ordered = sorted(values)
    middle = len(ordered) // 2
    if not ordered:
        raise ValueError("cannot compute median of empty sequence")
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2.0


def _mean(values: Iterable[float]) -> float:
    total = sum(values)
    count = len(values)
    if not count:
        raise ValueError("cannot compute mean of empty sequence")
    return total / count


def _standard_deviation(values: Iterable[float], population: bool = False) -> float:
    count = len(values)
    if count < 2:
        raise ValueError("standard deviation needs at least two values")
    average = _mean(values)
    squared_deviations = [
        (value - average) ** 2 for value in values
    ]
    divisor = count if population else count - 1
    variance = sum(squared_deviations) / divisor
    return variance ** 0.5


def detect_anomalies(
    field_values: Iterable[float],
    threshold_multiplier: float = 3.0,
    z_score_threshold: float = 3.0,
) -> List[Optional[float]]:
    """Flag suspicious values in a numeric field using simple statistics.

    A value is reported as anomalous when it lies more than
    ``threshold_multiplier`` standard deviations away from the mean, or when its
    z-score exceeds ``z_score_threshold`` in absolute value.
    """
    values = list(field_values)
    if len(values) < 2:
        return []

    average = _mean(values)
    spread = _standard_deviation(values)
    if spread == 0:
        return []

    anomalies: List[Optional[float]] = []
    for value in values:
        distance = abs(value - average)
        if distance > threshold_multiplier * spread:
            anomalies.append(value)
        z_score = (value - average) / spread
        if abs(z_score) > z_score_threshold:
            anomalies.append(value)
    return anomalies
