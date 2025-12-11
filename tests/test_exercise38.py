import pytest

from exercises.exercise38_KillerSudoku import KillerSudoku


# ----------------------------------
# Basic tests: total = value, 1 cell
# ----------------------------------
@pytest.mark.parametrize(
    "total, size, forbidden, expected",
    [
        (1, 1, [], [(1,)]),
        (2, 1, [], [(2,)]),
        (3, 1, [], [(3,)]),
        (4, 1, [], [(4,)]),
        (5, 1, [], [(5,)]),
        (6, 1, [], [(6,)]),
        (7, 1, [], [(7,)]),
        (8, 1, [], [(8,)]),
        (9, 1, [], [(9,)]),
    ],
)
def test_single_cell_combinations(
    total: int,
    size: int,
    forbidden: list[int],
    expected: list[tuple[int, ...]],
) -> None:
    result: list[tuple[int, ...]] = KillerSudoku(total, size, forbidden)

    assert result == expected, (
        f"Error testing single cell: "
        f"KillerSudoku({total}, {size}, {forbidden}) returned {result}, "
        f"but expected {expected}"
    )


# ----------------------------------
# Test for total sum 45 with 9 cells
# ----------------------------------
def test_cage_with_sum_45_contains_all_digits_1_9() -> None:
    result: list[tuple[int, ...]] = KillerSudoku(45, 9, [])
    expected: list[tuple[int, ...]] = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]

    assert result == expected, (
        f"Error in cage with sum 45 and 9 cells: "
        f"returned {result}, but expected {expected}"
    )


# ----------------------------------
# Test with only one possible combination
# ----------------------------------
def test_cage_with_only_one_possible_combination() -> None:
    result: list[tuple[int, ...]] = KillerSudoku(7, 3, [])
    expected: list[tuple[int, ...]] = [(1, 2, 4)]

    assert result == expected, (
        f"Error testing single possible combination: "
        f"returned {result}, but expected {expected}"
    )


# ----------------------------------
# Tests with multiple combinations (with and without restriction)
# ----------------------------------
@pytest.mark.parametrize(
    "total, size, forbidden, expected",
    [
        (10, 2, [], [(1, 9), (2, 8), (3, 7), (4, 6)]),
        (10, 2, [1, 4], [(2, 8), (3, 7)]),
    ],
)
def test_cage_with_multiple_combinations(
    total: int,
    size: int,
    forbidden: list[int],
    expected: list[tuple[int, ...]],
) -> None:
    result: list[tuple[int, ...]] = KillerSudoku(total, size, forbidden)

    assert result == expected, (
        f"Error in multiple combinations: "
        f"KillerSudoku({total}, {size}, {forbidden}) returned {result}, "
        f"but expected {expected}"
    )
