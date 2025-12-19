# Power Digit Sum
# Problem 16

# 2¹⁵ = 32768 and 3+2+7+8 = 26
# What is the sum of the digits of the number 2¹⁰⁰⁰


def power_digit_sum(
    power: int,
) -> int:
    """
    Compute the sum of the digits of the number 2 raised to a given power.

    This function calculates 2**power, converts the result to a string,
    and sums each digit of the resulting number.

    Parameters
    ----------
    power : int
        The exponent to which 2 is raised.

    Returns
    -------
    int
        The sum of the digits of 2**power.
    """
    return sum(int(digit) for digit in str(2 ** (power)))


def power(
    power: int,
) -> int:
    """
    Compute the sum of the digits of the number 2 raised to a given power
    using integer arithmetic.

    This function calculates 2**power and iteratively extracts each digit
    using modulo and integer division, accumulating their sum.

    Parameters
    ----------
    power : int
        The exponent to which 2 is raised.

    Returns
    -------
    int
        The sum of the digits of 2**power.
    """
    result = 0
    number = 2**power

    while number > 0:
        result += number % 10
        number //= 10

    return result
