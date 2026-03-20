import pytest

from exercises.exercise44_TwoBucket import TwoBucket


def test_measure_3_5_goal_1_start_one() -> None:
    assert TwoBucket(3, 5).measure(1, "one") == (4, "one", 5)


def test_measure_3_5_goal_1_start_two() -> None:
    assert TwoBucket(3, 5).measure(1, "two") == (8, "two", 3)


def test_measure_7_11_goal_2_start_one() -> None:
    assert TwoBucket(7, 11).measure(2, "one") == (14, "one", 11)


def test_measure_7_11_goal_2_start_two() -> None:
    assert TwoBucket(7, 11).measure(2, "two") == (18, "two", 7)


def test_measure_1_3_goal_3_start_two() -> None:
    assert TwoBucket(1, 3).measure(3, "two") == (1, "two", 0)


def test_measure_2_3_goal_3_start_one_end_TwoBucket_two() -> None:
    assert TwoBucket(2, 3).measure(3, "one") == (4, "two", 1)


def test_TwoBucket_one_much_bigger_than_two() -> None:
    assert TwoBucket(5, 1).measure(2, "one") == (6, "one", 1)


def test_TwoBucket_one_much_smaller_than_two() -> None:
    assert TwoBucket(3, 15).measure(9, "one") == (6, "two", 0)


def test_not_possible_to_reach_goal() -> None:
    with pytest.raises(ValueError):
        TwoBucket(6, 15).measure(5, "one")


def test_same_TwoBuckets_different_goal_possible() -> None:
    assert TwoBucket(6, 15).measure(9, "one") == (10, "two", 0)


def test_goal_larger_than_both_TwoBuckets_impossible() -> None:
    with pytest.raises(ValueError):
        TwoBucket(5, 7).measure(8, "one")
