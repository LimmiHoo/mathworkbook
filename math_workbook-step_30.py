# === Stage 30: Взвешенный рейтинг ===
# Project: MathWorkbook
def compute_problem_quality(condition, topic, difficulty, status,
                            weight_condition=0.35,
                            weight_topic=0.25,
                            weight_difficulty=0.20,
                            weight_status=0.20):
    """
    Compute a weighted quality score for a math problem.

    The score combines four indicators (condition, topic, difficulty, status)
    using configurable weights. All weights are normalized before use so the
    result stays bounded regardless of the input values.

    Args:
        condition: numeric indicator describing how well the problem is stated.
        topic: numeric indicator describing the topical relevance.
        difficulty: numeric indicator describing the difficulty level.
        status: numeric indicator describing the current status.
        weight_condition: weight for the condition indicator.
        weight_topic: weight for the topic indicator.
        weight_difficulty: weight for the difficulty indicator.
        weight_status: weight for the status indicator.

    Returns:
        A single weighted score.
    """
    raw_weights = [weight_condition, weight_topic,
                   weight_difficulty, weight_status]
    total_weight = sum(raw_weights)

    if total_weight <= 0:
        return 0.0

    normalized_weights = [w / total_weight for w in raw_weights]

    score = (
        normalized_weights[0] * condition
        + normalized_weights[1] * topic
        + normalized_weights[2] * difficulty
        + normalized_weights[3] * status
    )

    return score
