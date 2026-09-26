import pytest

from ml_foundations.split import sequential_split


def test_split_is_deterministic() -> None:
    assert sequential_split([1, 2, 3, 4, 5], 0.4) == ([1, 2, 3], [4, 5])


def test_split_rejects_invalid_ratio() -> None:
    with pytest.raises(ValueError):
        sequential_split([1, 2], 1)
