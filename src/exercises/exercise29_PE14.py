# Problem 14
# Longest Collatz Sequence

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

# Qual o starting number (<one million) que produz a cadeia mais longa?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def longest_collatz_sequence(
    number: int,
) -> int:
    """
    Finds the starting number (from 2 up to `number`) that produces the longest Collatz sequence.

    The Collatz sequence is defined as:
        - If n is even, n → n / 2
        - If n is odd,  n → 3n + 1
      Repeating this process eventually reaches 1 for all tested numbers.

    This function uses memoization (via a dictionary) to store already computed sequence lengths,
    which makes the algorithm much faster by avoiding repeated calculations.

    Args:
        number (int): The upper limit (inclusive) of numbers to check.

    Returns:
        int: The starting number below or equal to `number` that generates
             the longest Collatz sequence.

    Example:
        >>> longest_collatz_sequence(20)
        19
    """
    length = 0
    starting_number = 0
    cheat_sheet = {1: 1}

    for visitor in range(2, number + 1):
        guide = visitor
        counter = 0

        while guide != 1 and guide not in cheat_sheet:
            if guide % 2 == 0:
                guide //= 2
            else:
                guide = 3 * guide + 1
            counter += 1

        cheat_sheet[visitor] = counter + cheat_sheet.get(guide, 0)

        # ex: colinha = {16: 5} number and steps
        # number = 13, o while para no 5, porque chegou no 16
        # já sabemos que o 16 é 5, então pro 13, 5+5 = 10

        if cheat_sheet[visitor] > length:
            length = cheat_sheet[visitor]
            starting_number = visitor

    return starting_number


# PARALELISMO E DECORATOR
# https://github.com/Fazendaaa/project-euler/blob/master/src/python/src/project_euler/first/problem_14.py
