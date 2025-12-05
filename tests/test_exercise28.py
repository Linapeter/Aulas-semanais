import pytest

from exercises.exercise28_RomanNumerals import roman


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (9, "IX"),
        (16, "XVI"),
        (27, "XXVII"),
        (48, "XLVIII"),
        (49, "XLIX"),
        (59, "LIX"),
        (66, "LXVI"),
        (93, "XCIII"),
        (141, "CXLI"),
        (163, "CLXIII"),
        (166, "CLXVI"),
        (402, "CDII"),
        (575, "DLXXV"),
        (666, "DCLXVI"),
        (911, "CMXI"),
        (1_024, "MXXIV"),
        (1_666, "MDCLXVI"),
        (3_000, "MMM"),
        (3_001, "MMMI"),
        (3_888, "MMMDCCCLXXXVIII"),
        (3_999, "MMMCMXCIX"),
    ],
)
def test_roman_numerals(
    number: int,
    expected: str,
) -> None:
    assert roman(number) == expected
