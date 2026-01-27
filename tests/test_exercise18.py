import pytest
from pytest import approx

from python.exercise18_RationalNumbers import Rational


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Rational(1, 2), Rational(2, 3), Rational(7, 6)),
        (Rational(1, 2), Rational(-2, 3), Rational(-1, 6)),
        (Rational(-1, 2), Rational(-2, 3), Rational(-7, 6)),
        (Rational(1, 2), Rational(-1, 2), Rational(0, 1)),
    ],
    ids=[
        "positive + positive",
        "positive + negative",
        "negative + negative",
        "additive inverse",
    ],
)
def test_add(a: Rational, b: Rational, expected: Rational) -> None:
    result: Rational = a + b
    assert result == expected, f"{a} + {b} returned {result}, expected {expected}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Rational(1, 2), Rational(2, 3), Rational(-1, 6)),
        (Rational(1, 2), Rational(-2, 3), Rational(7, 6)),
        (Rational(-1, 2), Rational(-2, 3), Rational(1, 6)),
        (Rational(1, 2), Rational(1, 2), Rational(0, 1)),
    ],
    ids=[
        "positive - positive",
        "positive - negative",
        "negative - negative",
        "subtract itself",
    ],
)
def test_subtract(a: Rational, b: Rational, expected: Rational) -> None:
    result: Rational = a - b
    assert result == expected, f"{a} - {b} returned {result}, expected {expected}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Rational(1, 2), Rational(2, 3), Rational(1, 3)),
        (Rational(-1, 2), Rational(2, 3), Rational(-1, 3)),
        (Rational(-1, 2), Rational(-2, 3), Rational(1, 3)),
        (Rational(1, 2), Rational(2, 1), Rational(1, 1)),
        (Rational(1, 2), Rational(1, 1), Rational(1, 2)),
        (Rational(1, 2), Rational(0, 1), Rational(0, 1)),
    ],
    ids=[
        "positive * positive",
        "negative * positive",
        "negative * negative",
        "multiply by reciprocal",
        "multiply by one",
        "multiply by zero",
    ],
)
def test_multiply(a: Rational, b: Rational, expected: Rational) -> None:
    result: Rational = a * b
    assert result == expected, f"{a} * {b} returned {result}, expected {expected}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Rational(1, 2), Rational(2, 3), Rational(3, 4)),
        (Rational(1, 2), Rational(-2, 3), Rational(-3, 4)),
        (Rational(-1, 2), Rational(-2, 3), Rational(3, 4)),
        (Rational(1, 2), Rational(1, 1), Rational(1, 2)),
    ],
    ids=[
        "positive / positive",
        "positive / negative",
        "negative / negative",
        "divide by one",
    ],
)
def test_division(a: Rational, b: Rational, expected: Rational) -> None:
    result: Rational = a / b
    assert result == expected, f"{a} / {b} returned {result}, expected {expected}"


# --- Absolute value ---


@pytest.mark.parametrize(
    "value, expected",
    [
        (Rational(1, 2), Rational(1, 2)),
        (Rational(-1, -2), Rational(1, 2)),
        (Rational(-1, 2), Rational(1, 2)),
        (Rational(1, -2), Rational(1, 2)),
        (Rational(0, 1), Rational(0, 1)),
        (Rational(2, 4), Rational(1, 2)),
    ],
    ids=[
        "positive",
        "double negative",
        "negative numerator",
        "negative denominator",
        "zero",
        "reducible fraction",
    ],
)
def test_absolute_value(value: Rational, expected: Rational) -> None:
    result: Rational = abs(value)
    assert result == expected, f"abs({value}) returned {result}, expected {expected}"


# --- Exponentiation of a rational number ---


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (Rational(1, 2), 3, Rational(1, 8)),
        (Rational(-1, 2), 3, Rational(-1, 8)),
        (Rational(3, 5), -2, Rational(25, 9)),
        (Rational(-3, 5), -2, Rational(25, 9)),
        (Rational(-3, 5), -3, Rational(-125, 27)),
        (Rational(0, 1), 5, Rational(0, 1)),
        (Rational(1, 1), 4, Rational(1, 1)),
        (Rational(1, 2), 0, Rational(1, 1)),
        (Rational(-1, 2), 0, Rational(1, 1)),
    ],
    ids=[
        "positive power",
        "negative base odd power",
        "negative exponent",
        "negative base even negative power",
        "negative base odd negative power",
        "zero base",
        "one base",
        "zero exponent",
        "zero exponent negative base",
    ],
)
def test_exponentiation(
    base: Rational,
    exponent: int,
    expected: Rational,
) -> None:
    result: Rational = base**exponent
    assert (
        result == expected
    ), f"{base} ** {exponent} returned {result}, expected {expected}"


# --- Exponentiation of a real number to a rational number ---


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (8, Rational(4, 3), 16.0),
        (9, Rational(-1, 2), 1 / 3),
        (2, Rational(0, 1), 1.0),
    ],
    ids=[
        "positive rational exponent",
        "negative rational exponent",
        "zero rational exponent",
    ],
)
def test_real_number_exponentiation(
    base: int,
    exponent: Rational,
    expected: float,
) -> None:
    result: float = base**exponent
    assert result == approx(
        expected, abs=1e-8
    ), f"{base} ** {exponent} returned {result}, expected approximately {expected}"


# --- Reduction to lowest terms ---


@pytest.mark.parametrize(
    "value, expected",
    [
        (Rational(2, 4), Rational(1, 2)),
        (Rational(3, -4), Rational(-3, 4)),
        (Rational(-4, 6), Rational(-2, 3)),
        (Rational(3, -9), Rational(-1, 3)),
        (Rational(0, 6), Rational(0, 1)),
        (Rational(-14, 7), Rational(-2, 1)),
        (Rational(13, 13), Rational(1, 1)),
    ],
    ids=[
        "reduce by gcd",
        "negative denominator",
        "negative numerator",
        "negative both",
        "zero numerator",
        "whole number negative",
        "identity fraction",
    ],
)
def test_reduce_to_lowest_terms(
    value: Rational,
    expected: Rational,
) -> None:
    assert (
        value == expected
    ), f"Rational reduction returned {value}, expected {expected}"
