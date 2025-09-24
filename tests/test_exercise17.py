import math

import pytest

from exercises.exercise17 import complex_numbers


# Real part
def test_real_part() -> None:
    assert complex_numbers(1, 0).real == 1
    assert complex_numbers(0, 1).real == 0
    assert complex_numbers(1, 2).real == 1


# Imaginary part
def test_imaginary_part() -> None:
    assert complex_numbers(1, 0).imaginary == 0
    assert complex_numbers(0, 1).imaginary == 1
    assert complex_numbers(1, 2).imaginary == 2


def test_imaginary_unit() -> None:
    assert complex_numbers(0, 1) * complex_numbers(0, 1) == complex_numbers(-1, 0)


# Addition
def test_add_purely_real_numbers() -> None:
    assert complex_numbers(1, 0) + complex_numbers(2, 0) == complex_numbers(3, 0)
    assert complex_numbers(0, 1) + complex_numbers(0, 2) == complex_numbers(0, 3)
    assert complex_numbers(1, 2) + complex_numbers(3, 4) == complex_numbers(4, 6)


# Subtraction
def test_subtract_purely_real_numbers() -> None:
    assert complex_numbers(1, 0) - complex_numbers(2, 0) == complex_numbers(-1, 0)
    assert complex_numbers(0, 1) - complex_numbers(0, 2) == complex_numbers(0, -1)
    assert complex_numbers(1, 2) - complex_numbers(3, 4) == complex_numbers(-2, -2)


# Multiplication
def test_multiply_purely_real_numbers() -> None:
    assert complex_numbers(1, 0) * complex_numbers(2, 0) == complex_numbers(2, 0)
    assert complex_numbers(0, 1) * complex_numbers(0, 2) == complex_numbers(-2, 0)
    assert complex_numbers(1, 2) * complex_numbers(3, 4) == complex_numbers(-5, 10)


# Division
def test_divide() -> None:
    assert complex_numbers(1, 0) / complex_numbers(2, 0) == (complex_numbers(0.5, 0))
    assert complex_numbers(0, 1) / complex_numbers(0, 2) == (complex_numbers(0.5, 0))
    assert complex_numbers(1, 2) / complex_numbers(3, 4) == (complex_numbers(0.44, 0.08))


# Absolute value
def test_absolute_value() -> None:
    assert abs(complex_numbers(5, 0)) == 5
    assert abs(complex_numbers(-5, 0)) == 5
    assert abs(complex_numbers(0, 5)) == 5
    assert abs(complex_numbers(0, -5)) == 5
    assert abs(complex_numbers(3, 4)) == 5


# Complex conjugate
def test_conjugate() -> None:
    assert complex_numbers(5, 0).conjugate() == complex_numbers(5, 0)
    assert complex_numbers(0, 5).conjugate() == complex_numbers(0, -5)
    assert complex_numbers(1, 1).conjugate() == complex_numbers(1, -1)


# Complex exponential function
def test_euler_s_identity_formula() -> None:
    assert complex_numbers(0, math.pi).exp() == pytest.approx(complex_numbers(-1, 0))


def test_exponential() -> None:
    assert complex_numbers(0, 0).exp() == (complex_numbers(1, 0))
    assert complex_numbers(1, 0).exp() == (complex_numbers(math.e, 0))


def test_exponential_of_a_number_with_real_and_imaginary_part() -> None:
    assert complex_numbers(math.log(2), math.pi).exp() == pytest.approx(complex_numbers(-2, 0))


def test_exponential_resulting_in_a_number_with_real_and_imaginary_part() -> None:
    assert complex_numbers(math.log(2) / 2, math.pi / 4).exp() == (complex_numbers(1, 1))


# Operations between real numbers and complex numbers
def test_todo_real_number_to_complex_number() -> None:
    assert complex_numbers(1, 2) + 5 == complex_numbers(6, 2)
    assert 5 + complex_numbers(1, 2) == complex_numbers(6, 2)
    assert complex_numbers(5, 7) - 4 == complex_numbers(1, 7)
    assert 4 - complex_numbers(5, 7) == complex_numbers(-1, -7)
    assert complex_numbers(2, 5) * 5 == complex_numbers(10, 25)
    assert 5 * complex_numbers(2, 5) == complex_numbers(10, 25)
    assert complex_numbers(10, 100) / 10 == (complex_numbers(1, 10))
    assert 5 / complex_numbers(1, 1) == (complex_numbers(2.5, -2.5))


# Additional tests
def test_equality_of_complex_numbers() -> None:
    assert complex_numbers(1, 2) == complex_numbers(1, 2)


def test_inequality_of_real_part() -> None:
    assert complex_numbers(1, 2) != complex_numbers(2, 2)


def test_inequality_of_imaginary_part() -> None:
    assert complex_numbers(1, 2) != complex_numbers(1, 1)
