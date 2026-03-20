# Problem 21 - Project Euler

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1,2,4,71; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10_000.

from collections import Counter

from exercises.exercise20_PrimesMultiples import multiples


def divisors_sum(number: int) -> int:
    """Compute the sum of proper divisors of a positive integer.

    This function calculates the sum of all proper divisors of `number`
    using its prime factorization. It relies on the multiplicative formula
    for the divisor sum function:

        σ(n) = ∏ (p^(a+1) - 1) / (p - 1)

    where n = ∏ p^a is the prime factorization of n.

    The function returns σ(n) - n, which corresponds to the sum of
    proper divisors (excluding the number itself).

    Parameters
    ----------
    number : int
        A positive integer.

    Returns
    -------
    int
        The sum of proper divisors of `number`.

    Notes
    -----
    - Requires `multiples(number)` to return the list of prime factors
      of `number`, including repetitions.
    - Time complexity depends on the efficiency of `multiples`.
    """
    factors = multiples(number)
    sigma = 1
    factors_counts = Counter(factors)

    for factor, exponent in factors_counts.items():
        sigma *= (factor ** (exponent + 1) - 1) // (factor - 1)

    return sigma - number


def sum_of_amicable_pairs(limit: int) -> int:
    """
    Calculate the sum of all amicable numbers under a given limit.

    This function computes the sum of all amicable numbers less than `limit`.
    Two numbers a and b form an amicable pair if:

        sum_proper_divisors(a) = b
        sum_proper_divisors(b) = a
        a ≠ b

    The function uses memoization to cache divisor sums for efficiency.

    Parameters
    ----------
    limit : int
        The upper bound (exclusive) for amicable numbers to consider.

    Returns
    -------
    int
        The sum of all amicable numbers under the specified limit.

    Notes
    -----
    - Uses a cache dictionary to store previously computed divisor sums.
    - Time complexity depends on the efficiency of `divisors_sum`.
    - Each amicable pair is counted once (both numbers in the pair are summed).
    - Only pairs where both numbers are under `limit` are included.

    Example
    -------
    >>> amicable_pairs(10_000)
    31626
    """
    cache: dict[int, int] = {}
    result = 0

    def put_cache(number: int) -> int:
        if number not in cache:
            cache[number] = divisors_sum(number)
        return cache[number]

    for a in range(1, limit):
        b = put_cache(a)
        if b != a and b < limit and divisors_sum(b) == a and a < b:
            result += a + b

    return result
