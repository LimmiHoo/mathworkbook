# === Stage 25: Прогноз сроков ===
# Project: MathWorkbook
from collections import deque


def predict_next_intervals(task, history_window=5):
    """Predict the next set of completion intervals for a task.

    The prediction is derived from the task's previous intervals. If the
    history is empty the function returns the same interval declared in the
    task metadata. Otherwise it applies a smoothing over the last
    ``history_window`` intervals and then produces a confidence band around
    the smoothed value.

    Parameters
    ----------
    task : dict
        Must expose ``intervals`` (list of numbers) and ``interval`` (the
        currently declared interval).
    history_window : int, optional
        Number of most recent intervals taken into account for the average.
        Defaults to 5.

    Returns
    -------
    dict
        Contains ``predicted_interval`` (float), ``min_interval`` (float),
        ``max_interval`` (float) and ``confidence`` (float in 0..1).
    """
    previous = deque(task.get("intervals", []), maxlen=history_window)
    if not previous:
        declared = float(task.get("interval", 1))
        return {
            "predicted_interval": declared,
            "min_interval": declared * 0.75,
            "max_interval": declared * 1.25,
            "confidence": 0.5,
        }

    values = [float(item) for item in previous if item is not None and item > 0]
    if not values:
        declared = float(task.get("interval", 1))
        return {
            "predicted_interval": declared,
            "min_interval": declared * 0.75,
            "max_interval": declared * 1.25,
            "confidence": 0.5,
        }

    mean = sum(values) / len(values)
    span = max(values) - min(values)
    if span == 0:
        confidence = 1.0
    else:
        confidence = max(0.0, 1.0 - (span / (mean if mean > 0 else span)) * 0.5)
    confidence = round(confidence, 4)

    predicted = round(mean, 4)
    lower = round(max(0.0, predicted * 0.8), 4)
    upper = round(predicted * 1.2, 4)

    return {
        "predicted_interval": predicted,
        "min_interval": lower,
        "max_interval": upper,
        "confidence": confidence,
    }


if __name__ == "__main__":
    sample = {
        "intervals": [4, 3, 5, 4, 4],
        "interval": 4,
    }
    print(predict_next_intervals(sample))
    empty = {"intervals": [], "interval": 2}
    print(predict_next_intervals(empty))
