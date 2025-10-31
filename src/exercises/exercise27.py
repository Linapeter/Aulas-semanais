# Project Euler

# Problem 13
# Large Sum

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


def large_sum(box: str) -> int:
    """Calculates the sum of all integers in a string and returns the first 10 digits of the total sum.

    Args:
        box (str): A string containing space-separated integer values.

    Returns:
        int: The first 10 digits of the resulting sum.
    """
    numbers = list(map(int, box.split()))
    sum_numbers = str(sum(numbers))

    return int(sum_numbers[0:10])
