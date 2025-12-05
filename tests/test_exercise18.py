
from pytest import approx

from exercises.exercise18_RationalNumbers import Rational


# --- Arithmetic ---

# Addition
def test_add() -> None:
    assert Rational(1, 2) + Rational(2, 3) == Rational(7, 6)
    assert Rational(1, 2) + Rational(-2, 3) == Rational(-1, 6)
    assert Rational(-1, 2) + Rational(-2, 3) == Rational(-7, 6)
    assert Rational(1, 2) + Rational(-1, 2) == Rational(0, 1)


# Subtraction
def test_subtract() -> None:
    assert Rational(1, 2) - Rational(2, 3) == Rational(-1, 6)
    assert Rational(1, 2) - Rational(-2, 3) == Rational(7, 6)
    assert Rational(-1, 2) - Rational(-2, 3) == Rational(1, 6)
    assert Rational(1, 2) - Rational(1, 2) == Rational(0, 1)


# Multiplication
def test_multiply() -> None:
    assert Rational(1, 2) * Rational(2, 3) == Rational(1, 3)
    assert Rational(-1, 2) * Rational(2, 3) == Rational(-1, 3)
    assert Rational(-1, 2) * Rational(-2, 3) == Rational(1, 3)
    assert Rational(1, 2) * Rational(2, 1) == Rational(1, 1)
    assert Rational(1, 2) * Rational(1, 1) == Rational(1, 2)
    assert Rational(1, 2) * Rational(0, 1) == Rational(0, 1)


# Division
def test_division() -> None:
    assert Rational(1, 2) / Rational(2, 3) == Rational(3, 4)
    assert Rational(1, 2) / Rational(-2, 3) == Rational(-3, 4)
    assert Rational(-1, 2) / Rational(-2, 3) == Rational(3, 4)
    assert Rational(1, 2) / Rational(1, 1) == Rational(1, 2)


# --- Absolute value ---

def test_absolute_value() -> None:
    assert abs(Rational(1, 2)) == Rational(1, 2)
    assert abs(Rational(-1, -2)) == Rational(1, 2)
    assert abs(Rational(-1, 2)) == Rational(1, 2)
    assert abs(Rational(1, -2)) == Rational(1, 2)
    assert abs(Rational(0, 1)) == Rational(0, 1)
    assert abs(Rational(2, 4)) == Rational(1, 2)


# --- Exponentiation of a rational number ---

def test_exponentiation() -> None:
    assert Rational(1, 2) ** 3 == Rational(1, 8)
    assert Rational(-1, 2) ** 3 == Rational(-1, 8)
    assert Rational(3, 5) ** -2 == Rational(25, 9)
    assert Rational(-3, 5) ** -2 == Rational(25, 9)
    assert Rational(-3, 5) ** -3 == Rational(-125, 27)
    assert Rational(0, 1) ** 5 == Rational(0, 1)
    assert Rational(1, 1) ** 4 == Rational(1, 1)
    assert Rational(1, 2) ** 0 == Rational(1, 1)
    assert Rational(-1, 2) ** 0 == Rational(1, 1)


# --- Exponentiation of a real number to a rational number ---

def test_exponentiation_of_a_real_number_to_a_rational_number() -> None:
    assert 8 ** Rational(4, 3) == approx(16.0, abs=1e-8)
    assert 9 ** Rational(-1, 2) == approx(0.3333333333333333, abs=1e-8)
    assert 2 ** Rational(0, 1)== approx(1.0, abs=1e-8)


# --- Reduction to lowest terms ---

def test_reduce_to_lowest_terms() -> None:
    assert Rational(2, 4) == Rational(1, 2)
    assert Rational(3, -4) == Rational(-3, 4)
    assert Rational(-4, 6) == Rational(-2, 3)
    assert Rational(3, -9) == Rational(-1, 3)
    assert Rational(0, 6) == Rational(0, 1)
    assert Rational(-14, 7) == Rational(-2, 1)
    assert Rational(13, 13) == Rational(1, 1)
