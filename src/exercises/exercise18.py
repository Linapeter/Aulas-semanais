import math


class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        self.numer = numer
        self.denom = denom

    def __eq__(self, other: "Rational") -> "Rational":
        if not isinstance(other, Rational):
            return other
        if other.denom < 0 and other.numer > 0:
            other.numer = (-1) * other.numer
            other.denom = (-1) * other.denom
        return Rational(
            numer= other.numer / (math.gcd(other.numer, other.denom)),
            denom= other.denom / (math.gcd(other.numer, other.denom)),
        )

    def __repr__(self) -> str:
        return f"{self.numer}/{self.denom}"

    # r₁ + r₂ = a₁/b₁ + a₂/b₂ = (a₁ * b₂ + a₂ * b₁) / (b₁ * b₂).
    def __add__(self, other: "Rational" | int | float) -> "Rational":
        if isinstance(other, Rational) and self.denom != other.denom:
            return Rational(
                numer=(self.numer * other.denom + other.numer * self.denom),
                denom=self.denom * other.denom,
            )
        if isinstance(other, Rational) and self.denom == other.denom:
            return Rational(
                numer=(self.numer * other.denom + other.numer * self.denom),
                denom=self.denom,
            )
        if isinstance(other, int):
            return Rational(numer=self.numer + (other * self.denom), denom=self.denom)
        raise ValueError(
            f"Operation add not defined for rational number and {type(other)}"
        )

    def __radd__(self, other: int) -> "Rational":
        return self.__add__(other)

    # r₁ - r₂ = a₁/b₁ - a₂/b₂ = (a₁ * b₂ - a₂ * b₁) / (b₁ * b₂).
    def __sub__(self, other: "Rational" | int | float) -> "Rational":
        if isinstance(other, Rational):
            return Rational(
                numer=(self.numer * other.denom - other.numer * self.denom),
                denom=(self.denom * other.denom),
            )
        if isinstance(other, int):
            return Rational(numer=self.numer - (other * self.denom), denom=self.denom)
        raise ValueError(
            f"Operation subtraction not defined for rational number and {type(other)}"
        )

    def __rsub__(self, other: int) -> "Rational":
        if isinstance(other, int):
            return Rational(numer=other * self.denom - self.numer, denom=self.denom)

    # r₂ = a₂/b₂ is r₁ * r₂ = (a₁ * a₂) / (b₁ * b₂).
    def __mul__(self, other: "Rational" | int) -> "Rational":
        if isinstance(other, Rational):
            return Rational(
                numer=self.numer * other.numer, denom=self.denom * other.denom
            )
        if isinstance(other, int):
            return Rational(numer=self.numer * other, denom=self.denom)
        raise ValueError(
            f"Operation multiplication not defined for rational number and {type(other)}"
        )

    def __rmul__(self, other: int) -> "Rational":
        return self.__mul__(other)

    # r₁ / r₂ = (a₁ * b₂) / (a₂ * b₁) if a₂ is not zero.
    def __truediv__(self, other: "Rational" | int) -> "Rational":
        if isinstance(other, Rational) and other.denom != 0:
            return Rational(
                numer=self.numer * other.denom, denom=other.numer * self.denom
            )
        if isinstance(other, int):
            return Rational(numer=self.numer, denom=self.denom * other)
        raise ValueError(
            f"Operation division not defined for rational number and {type(other)}"
        )

    def __rtruediv__(self, other) -> "Rational":
        if isinstance(other, int):
            return Rational(numer=other * self.denom, denom=self.numer)

    def __abs__(self) -> "Rational":
        return Rational(numer=abs(self.numer), denom=abs(self.denom))

    # r^n = (a^n)/(b^n).
    def __pow__(self, power: int | float) -> "Rational":
        if isinstance(power, (int, float)) and power > 0:
            return Rational(
                numer=self.numer ** abs(power), denom=self.denom ** abs(power)
            )
        if isinstance(power, (int, float)) and power < 0:
            return Rational(numer=self.denom**power, denom=self.numer**power)
        if power == 0:
            return Rational(1,1)
        raise ValueError(
            f"Operation pow not defined for rational number and {type(power)}"
        )

    def __rpow__(self, base: int) -> float:
        if isinstance(base, int):
            return base ** (self.numer / self.denom)


print(Rational(1, 2) + Rational(-1, 2))
print(Rational(0,2))
