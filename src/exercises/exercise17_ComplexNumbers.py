from __future__ import annotations

from math import cos, exp, sin, sqrt
from typing import Any

# https://satish-p.medium.com/the-magic-of-python-a-comprehensive-guide-to-magic-methods-743bdeb4651f
# https://www.geeksforgeeks.org/python/dunder-magic-methods-python/


class complex_numbers:
    """
    Represent complex numbers and support basic arithmetic operations.

    This class implements complex number arithmetic using Python magic
    methods, allowing instances to behave like built-in numeric types.
    """

    def __init__(
        self,
        real: float,
        imaginary: float,
    ) -> None:
        """
        Initialize a complex number.

        Parameters
        ----------
        real : float
            The real part of the complex number.
        imaginary : float
            The imaginary part of the complex number.
        """
        self.real = real
        self.imaginary = imaginary

    def __repr__(self) -> str:
        """
        Return a string representation of the complex number.

        Returns
        -------
        str
            The complex number in the form 'a + bi'.
        """
        return f"{self.real} + {self.imaginary}i"

    def __eq__(
        self,
        other: object,
    ) -> bool:
        """
        Check equality between two complex numbers.

        Parameters
        ----------
        other : object
            Another object to compare with.

        Returns
        -------
        bool
            True if both real and imaginary parts are equal.

        Raises
        ------
        ValueError
            If comparison is attempted with a non-complex_numbers object.
        """
        if not isinstance(other, complex_numbers):
            raise ValueError(
                f"Comparison with {type(other)} can not be made with complex_numbers"
            )
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(self) -> complex_numbers:
        """
        Return the complex conjugate.

        Returns
        -------
        complex_numbers
            A new complex number with the imaginary part negated.
        """
        return complex_numbers(real=self.real, imaginary=-self.imaginary)

    def __abs__(self) -> float:
        """
        Return the magnitude (modulus) of the complex number.

        Returns
        -------
        float
            The magnitude of the complex number.
        """
        return sqrt(self.real**2 + self.imaginary**2)

    def __add__(
        self,
        add: Any,
    ) -> complex_numbers:
        """
        Add a complex number or a real scalar.

        Parameters
        ----------
        add : Any
            A complex_numbers instance or a real number.

        Returns
        -------
        complex_numbers
            The result of the addition.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """
        if isinstance(add, complex_numbers):
            return complex_numbers(
                real=self.real + add.real, imaginary=self.imaginary + add.imaginary
            )
        if isinstance(add, (float, int)):
            return complex_numbers(real=self.real + add, imaginary=self.imaginary)
        raise ValueError(
            f"Operation add not defined for complex_numbers and {type(add)}"
        )

    def __radd__(
        self,
        other: int,
    ) -> complex_numbers:
        """
        Support right-hand addition with real numbers.

        Returns
        -------
        complex_numbers
            The result of the addition.
        """
        return self.__add__(other)

    def __sub__(
        self,
        sub: Any,
    ) -> complex_numbers:
        """
        Subtract a complex number or a real scalar.

        Parameters
        ----------
        sub : Any
            A complex_numbers instance or a real number.

        Returns
        -------
        complex_numbers
            The result of the subtraction.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """
        if isinstance(sub, complex_numbers):
            return complex_numbers(
                real=self.real - sub.real, imaginary=self.imaginary - sub.imaginary
            )
        if isinstance(sub, (float, int)):
            return complex_numbers(real=self.real - sub, imaginary=self.imaginary)
        raise ValueError(
            f"Operation sub not defined for complex_numbers and {type(sub)}"
        )

    def __rsub__(
        self,
        sub: int,
    ) -> complex_numbers:
        """
        Support right-hand subtraction with real numbers.

        Returns
        -------
        complex_numbers
            The result of the subtraction.
        """
        return complex_numbers(real=sub - self.real, imaginary=-self.imaginary)

    def __mul__(
        self,
        product: Any,
    ) -> complex_numbers:
        """
        Multiply by another complex number or a real scalar.

        Parameters
        ----------
        product : Any
            A complex_numbers instance or a real number.

        Returns
        -------
        complex_numbers
            The result of the multiplication.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """
        if isinstance(product, complex_numbers):
            real_part = self.real * product.real - self.imaginary * product.imaginary
            imaginary_part = (
                self.real * product.imaginary + self.imaginary * product.real
            )
            return complex_numbers(real=real_part, imaginary=imaginary_part)

        if isinstance(product, (int, float)):
            real_part = self.real * product
            imaginary_part = self.imaginary * product

            return complex_numbers(real=real_part, imaginary=imaginary_part)

        raise ValueError(
            f"Operation multiplication not defined for complex_numbers and {type(product)}"
        )

    def __rmul__(
        self,
        product: int,
    ) -> complex_numbers:
        """
        Support right-hand multiplication with real numbers.

        Returns
        -------
        complex_numbers
            The result of the multiplication.
        """
        return self.__mul__(product)

    def reciprocal(self) -> complex_numbers:
        """
        Return the multiplicative inverse of the complex number.

        Returns
        -------
        complex_numbers
            The reciprocal of the complex number.
        """
        return complex_numbers(
            real=self.real / (self.real**2 + self.imaginary**2),
            imaginary=-self.imaginary / (self.real**2 + self.imaginary**2),
        )

    def __truediv__(
        self,
        div: Any,
    ) -> complex_numbers:
        """
        Divide by another complex number or a real scalar.

        Parameters
        ----------
        div : Any
            A complex_numbers instance or a real number.

        Returns
        -------
        complex_numbers
            The result of the division.

        Raises
        ------
        ValueError
            If the operation is not defined for the given type.
        """
        if isinstance(div, complex_numbers):
            return complex_numbers(
                real=(self.real * div.real + self.imaginary * div.imaginary)
                / (div.real**2 + div.imaginary**2),
                imaginary=(self.imaginary * div.real - self.real * div.imaginary)
                / (div.real**2 + div.imaginary**2),
            )
        if isinstance(div, (float, int)):
            return complex_numbers(real=self.real / div, imaginary=self.imaginary / div)
        raise ValueError(
            f"Operation division not defined for complex_numbers and {type(div)}"
        )

    def __rtruediv__(
        self,
        div: int,
    ) -> complex_numbers:
        """
        Support right-hand division by a real number.

        Returns
        -------
        complex_numbers
            The result of the division.
        """
        return complex_numbers(
            real=(div * self.real) / (self.real**2 + self.imaginary**2),
            imaginary=(-div * self.imaginary) / (self.real**2 + self.imaginary**2),
        )

    def exp(self) -> complex_numbers:
        """
        Compute the complex exponential.

        Uses Euler's formula:
        exp(a + bi) = exp(a) * (cos(b) + i sin(b))

        Returns
        -------
        complex_numbers
            The exponential of the complex number.
        """
        return complex_numbers(
            real=exp(self.real) * cos(self.imaginary),
            imaginary=(exp(self.real) * sin(self.imaginary)),
        )
