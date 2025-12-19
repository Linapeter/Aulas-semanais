from math import pi

import pytest
from pytest import approx

from exercises.exercise17_ComplexNumbers import complex_numbers


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ((1, 0), (2, 0), (3, 0)),
        ((0, 1), (0, 2), (0, 3)),
        ((1, 2), (3, 4), (4, 6)),
    ],
)
def test_addition(
    a: tuple[float, float], b: tuple[float, float], expected: tuple[float, float]
) -> None:
    assert complex_numbers(*a) + complex_numbers(*b) == complex_numbers(*expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ((1, 0), (2, 0), (-1, 0)),
        ((0, 1), (0, 2), (0, -1)),
        ((1, 2), (3, 4), (-2, -2)),
    ],
)
def test_subtraction(
    a: tuple[float, float], b: tuple[float, float], expected: tuple[float, float]
) -> None:
    assert complex_numbers(*a) - complex_numbers(*b) == complex_numbers(*expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ((1, 0), (2, 0), (2, 0)),
        ((0, 1), (0, 2), (-2, 0)),
        ((1, 2), (3, 4), (-5, 10)),
    ],
)
def test_multiplication(
    a: tuple[float, float], b: tuple[float, float], expected: tuple[float, float]
) -> None:
    assert complex_numbers(*a) * complex_numbers(*b) == complex_numbers(*expected)


def test_exponential_eulers_identity() -> None:
    result = complex_numbers(0, pi).exp()
    assert result.real == approx(-1.0)
    assert result.imaginary == approx(0.0)
