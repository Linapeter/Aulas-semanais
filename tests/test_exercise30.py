import pytest

from exercises.exercise30_PhoneNumber import PhoneNumber


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("(223) 456-7890", "2234567890"),
        ("223.456.7890", "2234567890"),
        ("223 456   7890   ", "2234567890"),
        ("12234567890", "2234567890"),
        ("+1 (223) 456-7890", "2234567890"),
    ],
    ids=[
        "parentheses and dash",
        "dots",
        "spaces",
        "leading country code",
        "country code with symbols",
    ],
)
def test_valid_numbers(
    input_text: str,
    expected: str,
) -> None:
    result: str = PhoneNumber(input_text).number()
    assert result == expected, (
        f"PhoneNumber({input_text!r}).number() returned {result!r}, "
        f"expected {expected!r}"
    )


@pytest.mark.parametrize(
    "input_text, error_message",
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
    ids=[
        "too few digits",
        "11 digits not starting with 1",
        "too many digits",
        "letters not allowed",
        "punctuation not allowed",
        "area code starts with zero",
        "area code starts with one",
        "exchange code starts with zero",
        "exchange code starts with one",
        "area code zero with country code",
        "area code one with country code",
        "exchange code zero with country code",
        "exchange code one with country code",
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
    result: str = number.area_code()
    expected: str = "223"
    assert result == expected, (
        f"PhoneNumber('2234567890').area_code() returned {result!r}, "
        f"expected {expected!r}"
    )


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("2234567890", "(223) 456-7890"),
        ("12234567890", "(223) 456-7890"),
    ],
    ids=[
        "pretty print without country code",
        "pretty print with country code",
    ],
)
def test_pretty_print(
    input_text: str,
    expected: str,
) -> None:
    number = PhoneNumber(input_text)
    result: str = number.pretty_print()
    assert result == expected, (
        f"PhoneNumber({input_text!r}).pretty_print() returned {result!r}, "
        f"expected {expected!r}"
    )
