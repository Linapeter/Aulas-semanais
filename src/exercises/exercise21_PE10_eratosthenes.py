# The sum of the primes below 10 is 2+3+5+7 = 17.
# Find the sum of all the primes below two million 2,000,000.

from typing import Any


def sieve_of_eratosthenes(number: int) -> list[Any] | list[int]:

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

    primes = sieve_of_eratosthenes(limit)

    return sum(primes)
