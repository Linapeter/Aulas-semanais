# Killer Sudoku

# A friend of yours is learning how to solve Killer Sudokus (rules below) but struggling to figure out which digits can go in a cage. They ask you to help them out by writing a small program that lists all valid combinations for a given cage, and any constraints that affect the cage.

# To make the output of your program easy to read, the combinations it returns must be sorted.

# Killer Sudoku Rules
# Standard Sudoku rules apply.
# The digits in a cage, usually marked by a dotted line, add up to the small number given in the corner of the cage.
# A digit may only occur once in a cage.

# https://sudokupad.app/HqTBn3Pr6R

from itertools import combinations


def KillerSudoku(target: int, size: int, exclude: list[int]) -> list[tuple[int,...]]:
    digits = [i for i in range(1, min(target, 9) + 1) if i not in exclude]
    combs = combinations(digits, size)  # list[tuples[int]]
    result: list[tuple[int,...]] = []

    result = [i for i in combs if sum(i) == target]

    return result
