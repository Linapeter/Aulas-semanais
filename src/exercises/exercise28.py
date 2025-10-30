# Roman Numerals

# To write a Roman numeral we use the following Latin letters, each of which has a value:

# M	    D	C	L	X	V	I
# 1000	500	100	50	10	5	1

#  cases: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

class Roman_numerals():
    LETTERS: dict[str,int] = {
    "M": 1_000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
    }
    def __init__(self, number:int) -> None:
        self.number = number
        if not (0 < self.number < 4_000) :
            raise ValueError("Number out of range")

    def roman(self) -> str:
        result = ''
        rest = self.number
        for letters, numbers in self.LETTERS.items():
            while rest >= numbers:
                result += letters
                rest -= numbers
        return result


# def roman(number: int) -> str:
#     if 0 < number and number > 3_999:
#         raise ValueError("Number out of range")
#     if 900 <= number < 1_000 or 400 <= number < 500:
#         return "C" + roman(number + 100)
#     elif 90 <= number < 100 or 40 <= number <= 50:
#         return "X" + roman(number + 10)
#     elif number == 9 or number == 4:
#         return "I" + roman(number + 1)
#     elif number >= 1_000:
#         return "M" + roman(number - 1_000)
#     elif number >= 500:
#         return "D" + roman(number - 500)
#     elif number >= 100:
#         return "C" + roman(number - 100)
#     elif number >= 50:
#         return "L" + roman(number - 50)
#     elif number >= 10:
#         return "X" + roman(number - 10)
#     elif number >= 5:
#         return "V" + roman(number - 5)
#     elif number >= 1:
#         return "I" + roman(number - 1)
#     return ""
