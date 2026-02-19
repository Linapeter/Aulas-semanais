from exercises.exercise41_PE20 import factorial_sum_digits

def test_exercises41() -> None:
    assert 27 == factorial_sum_digits(10), "Broke in sum of digits of factorial of 10"
    assert 648 == factorial_sum_digits(100), "Broke in sum of digits of factorial of 100"