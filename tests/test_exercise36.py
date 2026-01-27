import pytest

from python.exercise36_ChangeCoins import find_fewest_coins


@pytest.mark.parametrize(
    "coins, target, expected",
    [
        ([1, 5, 10, 25], 1, [1]),
        ([1, 5, 10, 25, 100], 25, [25]),
        ([1, 5, 10, 25, 100], 15, [5, 10]),
        ([1, 4, 15, 20, 50], 23, [4, 4, 15]),
        ([1, 5, 10, 21, 25], 63, [21, 21, 21]),
        (
            [1, 2, 5, 10, 20, 50, 100],
            999,
            [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100],
        ),
        ([2, 5, 10, 20, 50], 21, [2, 2, 2, 5, 10]),
        ([4, 5], 27, [4, 4, 4, 5, 5, 5]),
        ([1, 5, 10, 21, 25], 0, []),
    ],
)
def test_change_valid_cases(coins: list[int], target: int, expected: list[int]) -> None:
    assert find_fewest_coins(coins, target) == expected, f"Failed on target = {target} with these coins = {coins}"

def test_exercise_coins() -> None:
    assert find_fewest_coins([1, 10, 11],20) == [10,10]

@pytest.mark.parametrize(
    "coins, target, message",
    [
        ([5, 10], 3, "can't make target with given coins"),
        ([5, 10], 94, "can't make target with given coins"),
    ],
)
def test_change_errors_cannot_make(coins: list[int], target: int, message: str) -> None:
    with pytest.raises(ValueError) as err:
        find_fewest_coins(coins, target)
    assert str(err.value) == message, "Failed identifying if it's possible make target with the given coins"


def test_negative_target_error() -> None:
    with pytest.raises(ValueError) as err:
        find_fewest_coins([1, 2, 5], -5)
    assert str(err.value) == "target can't be negative"
