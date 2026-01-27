from python.exercise33_PE16 import power_digit_sum,power

def test_function1() -> None:
    assert 26 == (power_digit_sum(15)), "Failed the first test"
    assert 1366 == (power_digit_sum(1_000)), "Failed the second test"

def test_function2() -> None:
    assert 26 == (power(15)), "Failed the first test"
    assert 1366 == (power(1_000)), "Failed the second test"