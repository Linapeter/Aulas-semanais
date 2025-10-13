# How To Spell Out Numbers

# Given a number, your task is to express it in English words exactly as your friend should say it out loud.
# Yaʻqūb expects to use numbers from 0 up to 999,999,999,999.
from typing import Any

from num2words import num2words


class spell_our_numbers:

    def __init__(self, number: Any) -> None:
        if not isinstance(number, int):
            raise ValueError("Input must be an integer.")
        if number < 0 or number > 999_999_999_999:
            raise ValueError("Input must be between 0 and 999,999,999,999.")
        self.number = number
        self.pick = str(self.number)
        self.digits = len(self.pick)

    def tens(self) -> Any:
        tens = int(self.pick[-2] + "0")
        units = int(self.pick[-1])
        if tens == 0 and units == 0:
            pass
        if tens == 0 and units != 0:
            return num2words(units)
        return f"{num2words(tens)}-{num2words(units)}"

    def hundreds(self) -> Any:  # 123
        hundreds = int(self.pick[-3])
        tens_units = int(self.pick[-3:])
        if tens_units == 0:
            if hundreds == 0:
                pass
            if hundreds != 0:
                return f"{num2words(hundreds)} hundred"
        else:
            return f"{num2words(hundreds)} hundred and {self.tens()}"

    def thousands(self) -> Any:  # 12_234
        thousands = int(self.pick[:-3])
        rest = int(self.pick[-3:])
        if rest == 0:
            if thousands == 0:
                pass
            if thousands != 0:
                return f"{num2words(thousands)} thousand"
        else:
            rest_int = str(rest)
            if len(str(rest_int)) <= 2:
                return f"{num2words(thousands)} thousand, {self.tens()}"
            if len(str(rest_int)) == 3:
                return f"{num2words(thousands)} thousand, {self.hundreds()}"

    def millions(self) -> Any:  # 1_234_567
        millions = int(self.pick[:-6])
        rest = int(self.pick[-6:])
        if rest == 0:
            return f"{num2words(millions)} million"
        if millions == 0 and rest == 0:
            pass
        else:
            if len(str(rest)) > 3:
                return f"{num2words(millions)} million, {self.thousands()}"

    def billions(self) -> Any:  # 1_234_567_890
        billions = int(self.pick[:-9])
        rest = int(self.pick[-9:])
        if rest == 0:
            return f"{num2words(billions)} billion"
        else:
            rest_int = str(rest)
            if len(rest_int) > 6:
                return f"{num2words(billions)} billion, {self.millions()}"
            if 3 < len(rest_int) <= 6:
                return f"{num2words(billions)} billion, {self.thousands()}"
            if len(rest_int) <= 3:
                return f"{num2words(billions)} billion, {self.hundreds()}"

    def say(self) -> Any:
        if self.digits == 1:
            return num2words(self.number)
        if self.digits == 2:
            return self.tens()
        if self.digits == 3:
            return self.hundreds()
        if 4 <= self.digits <= 6:
            return self.thousands()
        if 7 <= self.digits <= 9:
            return self.millions()
        if 10 <= self.digits <= 12:
            return self.billions()
