# Exercise 6: Sum squares difference

def sum_squares_difference(limit:int) -> int:
    """This function returns the difference between Sum of squares and Square of sums, beginning on 1 until limit.

    Args:
        limit (int)

    Returns:
        int
    """
    triangle = int(limit * (limit+1)/2)
    sum_of_squares = int((limit * (limit+1) * (2*limit+1)) / 6)

    return (triangle*triangle - sum_of_squares)
