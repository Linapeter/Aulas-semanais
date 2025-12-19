import pytest

from exercises.exercise22_SpellOutNumbers import spell_our_numbers


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "zero"),
        (1, "one"),
        (14, "fourteen"),
        (20, "twenty"),
        (22, "twenty-two"),
        (30, "thirty"),
        (99, "ninety-nine"),
        (100, "one hundred"),
        (123, "one hundred twenty-three"),
        (170, "one hundred seventy"),
        (200, "two hundred"),
        (999, "nine hundred ninety-nine"),
        (1_000, "one thousand"),
        (1_234, "one thousand, two hundred thirty-four"),
        (1_000_000, "one million"),
        (
            1_002_345,
            "one million, two thousand, three hundred forty-five",
        ),
        (1_000_000_000, "one billion"),
        (
            987_654_321_123,
            "nine hundred eighty-seven billion, six hundred fifty-four million, "
            "three hundred twenty-one thousand, one hundred twenty-three",
        ),
    ],
    ids=[
        "zero",
        "one",
        "fourteen",
        "twenty",
        "twenty-two",
        "thirty",
        "ninety-nine",
        "one hundred",
        "one hundred twenty-three",
        "one hundred seventy",
        "two hundred",
        "nine hundred ninety-nine",
        "one thousand",
        "one thousand two hundred thirty-four",
        "one million",
        "one million two thousand three hundred forty-five",
        "one billion",
        "very large number",
    ],
)
def test_spell_out_numbers(
    number: int,
    expected: str,
) -> None:
    result: str = spell_our_numbers(number).say()
    assert result == expected, (
        f"spell_our_numbers({number}).say() returned {result!r}, "
        f"expected {expected!r}"
    )


@pytest.mark.parametrize(
    "number",
    [
        -1,
        1_000_000_000_000,
    ],
    ids=[
        "below zero",
        "above maximum allowed",
    ],
)
def test_numbers_out_of_range(
    number: int,
) -> None:
    with pytest.raises(ValueError) as err:
        spell_our_numbers(number).say()

    assert (
        err.type is ValueError
    ), f"spell_our_numbers({number}) did not raise ValueError"

    assert err.value.args[0] in {"Input out of range.", "input out of range"}, (
        f"spell_our_numbers({number}) raised ValueError with message "
        f"{err.value.args[0]!r}, expected 'Input out of range.'"
    )
