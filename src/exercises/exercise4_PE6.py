# Exercise 6: Sum squares difference


def sum_squares_difference(limit: int) -> int:
    """This function returns the difference between Sum of squares and Square of sums, beginning on 1 until limit.

    Args:
        limit (int)

    Returns:
        int
    """
    return (int(limit * (limit + 1) / 2))**2 - int((limit * (limit + 1) * (2 * limit + 1)) / 6)
