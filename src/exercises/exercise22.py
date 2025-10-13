# How To Spell Out Numbers

# Given a number, your task is to express it in English words exactly as your friend should say it out loud.
# Yaʻqūb expects to use numbers from 0 up to 999,999,999,999.
from typing import Any

from num2words import num2words


class spell_our_numbers:

    def __init__(self, number: int) -> None:
        if number < 0 or number >= 10**12:
            raise ValueError("Input out of range.")
        self.number = number

    def say(self, value: int = None) -> str:
        if not value:
            value = self.number

        if value == 0:
            return "zero"

        if value >= 1_000:
            scales = [
                (1_000_000_000, "billion"),
                (1_000_000, "million"),
                (1_000, "thousand"),
            ]

            for scale_value, scale_name in scales:
                if value >= scale_value:
                    before_scale = self.say(value // scale_value)
                    after_scale = value % scale_value
                    result = before_scale + " " + scale_name
                    if after_scale > 0:
                        result += ", " + num2words(after_scale)
                    return result
        if value < 1_000:
            result = ""

            if value >= 100:
                result += num2words(value // 100) + " hundred"
                value %= 100
                if value > 0:
                    result += " "

            if value >= 20:
                result += num2words(value // 10 * 10)
                if value % 10 > 0:
                    result += "-" + num2words(value % 10)
            elif value > 0:
                result += num2words(value)

        return result
