from math import gcd
from typing import Any


class Rational:
    """
    Represent rational numbers and support arithmetic operations.

    A rational number is represented as a fraction (numerator/denominator)
    and is always kept in its reduced (simplified) form.
    """

    def __init__(
        self,
        numerator: int | float,
        denominator: int | float,
    ) -> None:
        """
        Initialize a rational number.

        Parameters
        ----------
        numerator : int | float
            The numerator of the rational number.
        denominator : int | float
            The denominator of the rational number.

        Raises
        ------
        ValueError
            If the denominator is zero.
        """
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.__summarize__()

    def __summarize__(self) -> None:
        """
        Normalize and simplify the rational number.

        This method:
        - Ensures the denominator is positive.
        - Reduces the fraction using the greatest common divisor (GCD).
        - Raises an error if the denominator is zero.

        Raises
        ------
        ValueError
            If the denominator is zero.
        """
        if (self.denominator < 0 and self.numerator > 0) or (
            self.numerator < 0 and self.denominator < 0
        ):
            self.numerator = (-1) * self.numerator
            self.denominator = (-1) * self.denominator
        divisor = gcd(self.numerator, self.denominator)
        if divisor != 1 and divisor != 0:
            self.numerator = int(self.numerator / divisor)
            self.denominator = int(self.denominator / divisor)
        if not self.denominator:
            raise ValueError("Denominator cannot be zero")

    def __eq__(
        self,
        other: object,
    ) -> bool:
        """
        Check equality between two rational numbers.

        Parameters
        ----------
        other : object
            Another object to compare with.

        Returns
        -------
        bool
            True if both numerator and denominator are equal.

        Raises
        ------
        ValueError
            If comparison is attempted with a non-Rational object.
        """
        if not isinstance(other, Rational):
            raise ValueError(
                f"Comparison with {type(other)} can not be made with Rational numbers"
            )
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __repr__(self) -> str:
        """
        Return a string representation of the rational number.

        Returns
        -------
        str
            The rational number in the form 'a/b'.
        """
        return f"{self.numerator}/{self.denominator}"

    # r₁ + r₂ = a₁/b₁ + a₂/b₂ = (a₁ * b₂ + a₂ * b₁) / (b₁ * b₂).
    def __add__(
        self,
        other: Any,
    ) -> "Rational":
        """
        Add another rational number or an integer.

        Parameters
        ----------
        other : Any
            A Rational instance or an integer.

        Returns
        -------
        Rational
            The result of the addition.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """

        if isinstance(other, Rational) and self.denominator != other.denominator:
            return Rational(
                numerator=(
                    self.numerator * other.denominator
                    + other.numerator * self.denominator
                ),
                denominator=self.denominator * other.denominator,
            )
        if isinstance(other, Rational) and self.denominator == other.denominator:
            return Rational(
                numerator=(
                    self.numerator * other.denominator
                    + other.numerator * self.denominator
                ),
                denominator=self.denominator,
            )
        if isinstance(other, int):
            return Rational(
                numerator=self.numerator + (other * self.denominator),
                denominator=self.denominator,
            )
        raise ValueError(
            f"Operation add not defined for rational number and {type(other)}"
        )

    def __radd__(
        self,
        other: int,
    ) -> "Rational":
        """
        Support right-hand addition with integers.
        """
        return self.__add__(other)

    # r₁ - r₂ = a₁/b₁ - a₂/b₂ = (a₁ * b₂ - a₂ * b₁) / (b₁ * b₂).
    def __sub__(
        self,
        other: Any,
    ) -> "Rational":
        """
        Subtract another rational number or an integer.

        Parameters
        ----------
        other : Any
            A Rational instance or an integer.

        Returns
        -------
        Rational
            The result of the subtraction.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """
        if isinstance(other, Rational):
            return Rational(
                numerator=(
                    self.numerator * other.denominator
                    - other.numerator * self.denominator
                ),
                denominator=(self.denominator * other.denominator),
            )
        if isinstance(other, int):
            return Rational(
                numerator=self.numerator - (other * self.denominator),
                denominator=self.denominator,
            )
        raise ValueError(
            f"Operation subtraction not defined for rational number and {type(other)}"
        )

    def __rsub__(
        self,
        other: int,
    ) -> "Rational":
        """
        Support right-hand subtraction with integers.
        """
        return Rational(
            numerator=other * self.denominator - self.numerator,
            denominator=self.denominator,
        )

    # r₂ = a₂/b₂ is r₁ * r₂ = (a₁ * a₂) / (b₁ * b₂).
    def __mul__(
        self,
        other: object,
    ) -> "Rational":
        """
        Multiply by another rational number or an integer.

        Parameters
        ----------
        other : object
            A Rational instance or an integer.

        Returns
        -------
        Rational
            The result of the multiplication.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """
        if isinstance(other, Rational):
            return Rational(
                numerator=self.numerator * other.numerator,
                denominator=self.denominator * other.denominator,
            )
        if isinstance(other, int):
            return Rational(
                numerator=self.numerator * other, denominator=self.denominator
            )
        raise ValueError(
            f"Operation multiplication not defined for rational number and {type(other)}"
        )

    def __rmul__(
        self,
        other: int,
    ) -> "Rational":
        """
        Support right-hand multiplication with integers.
        """
        return self.__mul__(other)

    # r₁ / r₂ = (a₁ * b₂) / (a₂ * b₁) if a₂ is not zero.
    def __truediv__(
        self,
        other: object,
    ) -> "Rational":
        """
        Divide by another rational number or an integer.

        Parameters
        ----------
        other : object
            A Rational instance or an integer.

        Returns
        -------
        Rational
            The result of the division.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """
        if isinstance(other, Rational) and other.denominator != 0:
            return Rational(
                numerator=self.numerator * other.denominator,
                denominator=other.numerator * self.denominator,
            )
        if isinstance(other, int):
            return Rational(
                numerator=self.numerator, denominator=self.denominator * other
            )
        raise ValueError(
            f"Operation division not defined for rational number and {type(other)}"
        )

    def __rtruediv__(
        self,
        other: int,
    ) -> "Rational":
        """
        Support right-hand division by an integer.
        """
        return Rational(numerator=other * self.denominator, denominator=self.numerator)

    def __abs__(self) -> "Rational":
        """
        Return the absolute value of the rational number.
        """
        return Rational(
            numerator=abs(self.numerator), denominator=abs(self.denominator)
        )

    # r^n = (a^n)/(b^n).
    def __pow__(
        self,
        power: int | float,
    ) -> "Rational":
        """
        Raise the rational number to a power.

        Parameters
        ----------
        power : int | float
            The exponent.

        Returns
        -------
        Rational
            The result of the exponentiation.

        Raises
        ------
        ValueError
            If the operation is not defined for the given power.
        """
        if power > 0:
            return Rational(
                numerator=self.numerator**power, denominator=self.denominator**power
            )
        if power < 0:
            return Rational(
                numerator=self.denominator ** abs(power),
                denominator=self.numerator ** abs(power),
            )
        if power == 0:
            return Rational(1, 1)
        raise ValueError(
            f"Operation pow not defined for rational number and {type(power)}"
        )

    def __rpow__(
        self,
        base: int,
    ) -> Any:
        """
        Support exponentiation with a rational exponent.

        Returns
        -------
        Any
            The result of raising the base to a rational power.
        """
        return base ** (self.numerator / self.denominator)
