import math

# https://satish-p.medium.com/the-magic-of-python-a-comprehensive-guide-to-magic-methods-743bdeb4651f
# https://www.geeksforgeeks.org/python/dunder-magic-methods-python/


class complex_numbers:

    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary

    def __repr__(self) -> str:
        return f"{self.real} + {self.imaginary}i"

    def __eq__(self, other: "complex_numbers") -> bool:
        if isinstance(other, complex_numbers):
            return self.real == other.real and self.imaginary == other.imaginary
        return False

    def conjugate(self) -> "complex_numbers":
        return complex_numbers(real=self.real, imaginary=-self.imaginary)

    def __abs__(self) -> float:
        absolute_value = math.sqrt(self.real**2 + self.imaginary**2)
        return absolute_value

    def __add__(self, add: "complex_numbers" | int | float) -> "complex_numbers":
        if isinstance(add, complex_numbers):
            return complex_numbers(
                real=self.real + add.real, imaginary=self.imaginary + add.imaginary
            )
        if isinstance(add, (float, int)):
            return complex_numbers(real=self.real + add, imaginary=self.imaginary)
        raise ValueError(
            f"Operation add not defined for complex_numbers and {type(add)}"
        )

    def __radd__(self, other: int) -> "complex_numbers":
        return self.__add__(other)

    def __sub__(self, sub: "complex_numbers" | int | float) -> "complex_numbers":
        if isinstance(sub, complex_numbers):
            return complex_numbers(
                real=self.real - sub.real, imaginary=self.imaginary - sub.imaginary
            )
        if isinstance(sub, (float, int)):
            return complex_numbers(real=self.real - sub, imaginary=self.imaginary)
        raise ValueError(
            f"Operation sub not defined for complex_numbers and {type(sub)}"
        )

    def __rsub__(self, sub: int) -> "complex_numbers":
        return complex_numbers(real=sub - self.real, imaginary=-self.imaginary)

    def __mul__(self, product: "complex_numbers" | int | float) -> "complex_numbers":
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

    def __rmul__(self, product: int) -> "complex_numbers":
        return self.__mul__(product)

    def reciprocal(self) -> "complex_numbers":
        return complex_numbers(
            real=self.real / (self.real**2 + self.imaginary**2),
            imaginary=-self.imaginary / (self.real**2 + self.imaginary**2),
        )

    def __truediv__(self, div: "complex_numbers" | int | float) -> "complex_numbers":
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

    def __rtruediv__(self, div: int) -> "complex_numbers":
        return complex_numbers(
            real=(div * self.real) / (self.real**2 + self.imaginary**2),
            imaginary=(-div * self.imaginary) / (self.real**2 + self.imaginary**2),
        )

    def exp(self) -> "complex_numbers":
        return complex_numbers(
            real=math.exp(self.real) * math.cos(self.imaginary),
            imaginary=(math.exp(self.real) * math.sin(self.imaginary)),
        )
