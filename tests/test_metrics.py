import pytest

from ml_foundations.metrics import accuracy_score


def test_accuracy_score() -> None:
    assert accuracy_score([1, 0, 1, 1], [1, 1, 1, 0]) == 0.5


def test_accuracy_rejects_mismatched_lengths() -> None:
    with pytest.raises(ValueError):
        accuracy_score([1], [])
