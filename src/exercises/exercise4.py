# Exercise 2: Sum squares difference

def sum_squares_difference(limit:int) -> int:
    """This function returns the difference between Sum of squares and Square of sums, beginning on 1 until limit.

    Args:
        limit (int)

    Returns:
        int
    """
    sum_of_squares = (sum(sum_of_squares**2 for sum_of_squares in range(1,limit+1)))
    square_of_sums = ((sum(i for i in range(1,limit+1)))**2)

    return (square_of_sums - sum_of_squares)