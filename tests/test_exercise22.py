from pytest import raises
from exercises.exercise22_SpellOutNumbers import spell_our_numbers

def test_zero() -> None:
    assert spell_our_numbers(0).say() == "zero"

def test_one() -> None:
    assert spell_our_numbers(1).say() == "one"

def test_fourteen() -> None:
    assert spell_our_numbers(14).say() == "fourteen"

def test_twenty() -> None:
    assert spell_our_numbers(20).say() == "twenty"

def test_twenty_two() -> None:
    assert spell_our_numbers(22).say() == "twenty-two"

def test_thirty() -> None:
    assert spell_our_numbers(30).say() == "thirty"

def test_ninety_nine() -> None:
    assert spell_our_numbers(99).say() == "ninety-nine"

def test_one_hundred() -> None:
    assert spell_our_numbers(100).say() == "one hundred"

def test_one_hundred_twenty_three() -> None:
    assert spell_our_numbers(123).say() == "one hundred twenty-three"

def test_two_hundred() -> None:
    assert spell_our_numbers(200).say() == "two hundred"

def test_nine_hundred_ninety_nine() -> None:
    assert spell_our_numbers(999).say() == "nine hundred ninety-nine"

def test_one_thousand() -> None:
    assert spell_our_numbers(1_000).say() == "one thousand"

def test_one_thousand_two_hundred_thirty_four() -> None:
    assert spell_our_numbers(1_234).say() == "one thousand, two hundred thirty-four"

def test_one_million() -> None:
    assert spell_our_numbers(1_000_000).say() == "one million"

def test_one_million_two_thousand_three_hundred_forty_five() -> None:
    assert spell_our_numbers(1_002_345).say() == "one million, two thousand, three hundred forty-five"

def test_one_billion() -> None:
    assert spell_our_numbers(1_000_000_000).say() == "one billion"

def test_a_big_number() -> None:
    assert spell_our_numbers(987_654_321_123).say() == (
        "nine hundred eighty-seven billion, six hundred fifty-four million, three hundred twenty-one thousand, one hundred twenty-three"
    )

def test_numbers_below_zero_are_out_of_range() -> None:
    with raises(ValueError) as err:
        spell_our_numbers(-1).say()
    assert err.type is ValueError
    assert err.value.args[0] == "Input out of range." or err.value.args[0] == "input out of range"

def test_numbers_above_999_999_999_999_are_out_of_range() -> None:
    with raises(ValueError) as err:
        spell_our_numbers(1_000_000_000_000).say()
    assert err.type is ValueError
    assert err.value.args[0] == "Input out of range." or err.value.args[0] == "input out of range"

def test_one_hundred_seventy() -> None:
    assert spell_our_numbers(170).say() == "one hundred seventy"
