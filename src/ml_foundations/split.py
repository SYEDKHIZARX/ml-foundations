from collections.abc import Sequence


def sequential_split[T](items: Sequence[T], validation_ratio: float = 0.2) -> tuple[list[T], list[T]]:
    """Create a deterministic holdout split for ordered experiment inputs."""
    if not 0 < validation_ratio < 1:
        raise ValueError("validation_ratio must be between 0 and 1")
    if len(items) < 2:
        raise ValueError("at least two items are required")
    cutoff = max(1, int(len(items) * (1 - validation_ratio)))
    return list(items[:cutoff]), list(items[cutoff:])
