# Power Digit Sum
# Problem 16

# 2¹⁵ = 32768 and 3+2+7+8 = 26
# What is the sum of the digits of the number 2¹⁰⁰⁰


def power_digit_sum(
    power: int,
) -> int:
    return sum(int(digit) for digit in str(2 ** (power)))


def power(
    power: int,
) -> int:
    result = 0
    number = 2**power

    while number > 0:
        result += number % 10
        number //= 10

    return result
