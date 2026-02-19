# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1,2,4,71; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10_000.

from exercises.exercise20_PrimesMultiples import multiples

def divisors_sum(number:int) -> int:
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

    for factor in set(factors):
        exponent = factors.count(factor)
        sigma *= (factor**(exponent + 1) - 1) // (factor - 1)

    return sigma - number

def amicable_pairs(number: int) -> int:
    """Determine whether a number is part of an amicable pair.

    Two numbers a and b form an amicable pair if:

        sum_proper_divisors(a) = b
        sum_proper_divisors(b) = a
        a ≠ b

    This function checks whether `number` satisfies this condition.
    If so, it returns its amicable partner. Otherwise, it returns 0.

    Parameters
    ----------
    number : int
        A positive integer.

    Returns
    -------
    int
        The amicable partner of `number` if it exists,
        otherwise 0.
    """
    b = divisors_sum(number)
    if b != number and divisors_sum(b) == number:
        return b
    return 0


def amicable(limit: int) -> int:
    """Compute the sum of all amicable numbers below a given limit.

    This function uses a sieve-like approach to efficiently compute
    the sum of proper divisors for all integers below `limit`.
    It then identifies amicable pairs and accumulates their values.

    An amicable pair (a, b) satisfies:
        d(a) = b
        d(b) = a
        a ≠ b

    where d(n) is the sum of proper divisors of n.

    Parameters
    ----------
    limit : int
        Upper bound (exclusive). Only numbers less than `limit`
        are considered.

    Returns
    -------
    int
        The sum of all amicable numbers below `limit`.

    Notes
    -----
    - Time complexity is approximately O(n log n) due to the sieve.
    - Each amicable number is counted once.
    """
    numbers = [0] * limit

    for i in range(1, limit // 2):
        for j in range(2 * i, limit, i):
            numbers[j] += i

    total = 0
    for a in range(2, limit):
        b = numbers[a]
        if a != b and b < limit and numbers[b] == a:
            total += a

    return total



# 1   +1
# 2   +1
# 3   +1
# 4   +1 +2
# 5   +1
# 6   +1 +2 +3
# 7   +1
# 8   +1 +2    +4
# 9   +1    +3
# 10  +1 +2       +5
# 11  +1
# 12  +1 +2 +3 +4    +6
# 13  +1
# 14  +1 +2             +7
# 15  +1    +3    +5
# 16  +1 +2    +4          +8
# 17  +1
# 18  +1 +2 +3       +6       +9
# 19  +1
# 20  +1 +2    +4 +5             +10