# https://projecteuler.net/problem=20

# Factorial Digit Sum

# n! means n x (n-1) x ... x 3 x 2 x 1.
# For example, 10! = 362880
# and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 = 27

# Find the sum of the digits in the number 100!

from math import factorial

def factorial_sum_digits(number: int) -> int:
    """
    Compute the sum of the digits of the factorial of a given number.

    This function calculates the factorial of the input integer and then
    returns the sum of all digits in its decimal representation.

    Parameters
    ----------
    number : int
        A non-negative integer whose factorial will be computed.

    Returns
    -------
    int
        The sum of the digits of the factorial of the given number.
    """
    return sum(int(digit) for digit in str(factorial(number)))
