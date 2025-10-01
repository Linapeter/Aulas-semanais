# Compute the prime factors of a given natural number.

# A prime number is only evenly divisible by itself and 1.

# Note that 1 is not a prime number.

# 2 * 2 * 3 * 5
# = 4 * 15
# = 60

from exercises.exercise5 import largest_prime


def multiples(number: int) -> list[int]:
    """
    Returns the list of prime factors of the given natural number.

    Args:
        number (int): The natural number to factorize.

    Returns:
        list[int]: A list of prime factors in ascending order.
    """
    multiples: list[int] = []
    clone = number

    while clone > 1:
        prime = largest_prime(clone)
        if not clone % prime:
            multiples.append(prime)
            clone //= prime

        else:
            clone -= 1

    return multiples[::-1]
