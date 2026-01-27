import pytest

from python.exercise20_PrimesMultiples import multiples


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, []),
        (2, [2]),
        (3, [3]),
        (9, [3, 3]),
        (4, [2, 2]),
        (8, [2, 2, 2]),
        (27, [3, 3, 3]),
        (625, [5, 5, 5, 5]),
        (6, [2, 3]),
        (12, [2, 2, 3]),
        (901_255, [5, 17, 23, 461]),
        (93_819_012_551, [11, 9_539, 894_119]),
    ],
)
def test_factors(number: int, expected: list[int]) -> None:
    assert multiples(number) == expected, f"Failed on finding multiples to {number}. Expected: {expected}"
