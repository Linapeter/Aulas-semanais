import pytest

from exercises.exercise30_PhoneNumber import PhoneNumber


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("(223) 456-7890", "2234567890"),
        ("223.456.7890", "2234567890"),
        ("223 456   7890   ", "2234567890"),
        ("12234567890", "2234567890"),
        ("+1 (223) 456-7890", "2234567890"),
    ],
)
def test_valid_numbers(
    input_text: str,
    expected: str,
) -> None:
    assert PhoneNumber(input_text).number() == expected


@pytest.mark.parametrize(
    "input_text,error_message",
    [
        ("123456789", "must not be fewer than 10 digits"),
        ("22234567890", "11 digits must start with 1"),
        ("321234567890", "must not be greater than 11 digits"),
        ("523-abc-7890", "letters not permitted"),
        ("523-@:!-7890", "punctuations not permitted"),
        ("(023) 456-7890", "area code cannot start with zero"),
        ("(123) 456-7890", "area code cannot start with one"),
        ("(223) 056-7890", "exchange code cannot start with zero"),
        ("(223) 156-7890", "exchange code cannot start with one"),
        ("1 (023) 456-7890", "area code cannot start with zero"),
        ("1 (123) 456-7890", "area code cannot start with one"),
        ("1 (223) 056-7890", "exchange code cannot start with zero"),
        ("1 (223) 156-7890", "exchange code cannot start with one"),
    ],
)
def test_invalid_numbers(
    input_text: str,
    error_message: str,
) -> None:
    with pytest.raises(ValueError, match=error_message):
        PhoneNumber(input_text).number()


def test_area_code() -> None:
    number = PhoneNumber("2234567890")
    assert number.area_code() == "223"


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("2234567890", "(223) 456-7890"),
        ("12234567890", "(223) 456-7890"),
    ],
)
def test_pretty_print(
    input_text: str,
    expected: str,
) -> None:
    number = PhoneNumber(input_text)
    assert number.pretty_print() == expected
