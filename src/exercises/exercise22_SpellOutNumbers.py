# How To Spell Out Numbers

# Given a number, your task is to express it in English words exactly as your friend should say it out loud.
# Yaʻqūb expects to use numbers from 0 up to 999,999,999,999.

from num2words import num2words


class spell_our_numbers:
    """"""

    def __init__(
        self,
        number: int,
    ) -> None:
        """
        Convert integers into their English word representation.

        This class supports numbers from 0 up to (but not including) 10^12.
        Large numbers are spelled recursively using the scales:
        thousand, million, and billion.
        """
        if number < 0 or number >= 10**12:
            raise ValueError("Input out of range.")
        self.number = number

    def say(
        self,
        value: int | None = None,
    ) -> str:
        """
        Return the English word representation of a number.

        If no value is provided, the instance number is spelled.
        The method works recursively to handle large numbers.

        Parameters
        ----------
        value : int | None, optional
            The number to be spelled. Defaults to the stored number.

        Returns
        -------
        str
            The number spelled out in English words.
        """
        if value is None:
            value = self.number

        if value == 0:
            return "zero"

        scales = [
            (1_000_000_000, "billion"),
            (1_000_000, "million"),
            (1_000, "thousand"),
        ]

        for scale_value, scale_name in scales:
            if value >= scale_value:
                before = self.say(value // scale_value)
                after = value % scale_value
                if after == 0:
                    return f"{before} {scale_name}"
                return f"{before} {scale_name}, {self.say(after)}"

        # value < 1000:
        result = ""

        if value >= 100:
            result += num2words(value // 100) + " hundred"
            value %= 100
            if value > 0:
                result += " "

        if value >= 20:
            tens = (value // 10) * 10
            result += num2words(tens)
            if value % 10 > 0:
                result += "-" + num2words(value % 10)
        elif value > 0:
            result += num2words(value)

        return result
