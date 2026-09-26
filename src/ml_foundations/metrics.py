from collections.abc import Sequence


def accuracy_score(actual: Sequence[int], predicted: Sequence[int]) -> float:
    """Calculate classification accuracy with explicit input validation."""
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have the same length")
    if not actual:
        raise ValueError("at least one observation is required")
    return sum(a == p for a, p in zip(actual, predicted)) / len(actual)
