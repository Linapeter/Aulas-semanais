# The sum of the primes below 10 is 2+3+5+7 = 17.
# Find the sum of all the primes below two million 2,000,000.

from typing import Any


def sieve_of_eratosthenes(number: int) -> list[Any] | list[int]:
    """
    Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.

    The algorithm works by iteratively marking the multiples of each prime
    number starting from 2.

    Parameters
    ----------
    number : int
        Upper limit (inclusive) for generating prime numbers.

    Returns
    -------
    list[int]
        A list of all prime numbers less than or equal to `number`.
        Returns an empty list if `number` is less than 2.
    """

    if number < 2:
        return []

    is_prime = [True] * (number + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 False

    for i in range(2, int(number**0.5) + 1):
        if is_prime[i]:
            for j in range(
                i * i, number + 1, i
            ):  # i=2, j=4,6,8... / i=3, j=9,12,15... / i=4, j=16,20,24...
                # i=5, j=25,30,35... / i=6, j=36,42,48...
                is_prime[j] = False

    return [i for i, prime in enumerate(is_prime) if prime]


def sum_of_prime(limit: int) -> int:
    """
    Compute the sum of all prime numbers up to a given limit.

    Parameters
    ----------
    limit : int
        Upper limit (inclusive) for summing prime numbers.

    Returns
    -------
    int
        The sum of all prime numbers less than or equal to `limit`.
        Returns 0 if there are no primes.
    """

    primes = sieve_of_eratosthenes(limit)

    return sum(primes)
