# Killer Sudoku

# A friend of yours is learning how to solve Killer Sudokus (rules below) but struggling to figure out which digits can go in a cage. They ask you to help them out by writing a small program that lists all valid combinations for a given cage, and any constraints that affect the cage.

# To make the output of your program easy to read, the combinations it returns must be sorted.

# Killer Sudoku Rules
# Standard Sudoku rules apply.
# The digits in a cage, usually marked by a dotted line, add up to the small number given in the corner of the cage.
# A digit may only occur once in a cage.

# https://sudokupad.app/HqTBn3Pr6R

from itertools import combinations


def KillerSudoku(target: int, size: int, exclude: list[int]) -> list[tuple[int, ...]]:
    """Generates all valid number combinations for a Killer Sudoku cage.

    In Killer Sudoku, a cage is defined by:
      - A required sum (`target`)
      - A number of cells (`size`)
      - A list of digits to exclude (usually digits already present in the same row/column/box)

    The function returns all possible combinations of digits (1 to 9) of
    length `size` that:
      - Are strictly increasing (because combinations avoid repetition)
      - Do not include digits listed in `exclude`
      - Sum exactly to `target`

    Args:
        target (int):
            The required sum of the cage.
        size (int):
            The number of cells (digits) in the cage.
        exclude (list[int]):
            Digits that cannot be used in the combination.

    Returns:
        list[tuple[int, ...]]:
            A list of all valid digit combinations (each combination is a tuple).

    Example:
        >>> KillerSudoku(target=10, size=2, exclude=[1, 3])
        [(4, 6)]
    """
    digits = [digit for digit in range(1, min(target, 9) + 1) if digit not in exclude]

    return [
        combination
        for combination in combinations(digits, size)
        if sum(combination) == target
    ]
