# Week 1

# Exercise 1
# Execute a code that returns the sum of multiples of 3 and 5 up to the number n
# Ex: with n=10, the multiples are [3,5,6,9] and the sum is 23


def multiples_3_and_5(limit: int) -> int:
    """this function returns the sum of the multiples of 3 and 5 until limit.

    Args:
        limit (int)

    Returns:
        int
    """
    total = 0
    for i in range(1, limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
