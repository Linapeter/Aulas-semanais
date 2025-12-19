from exercises.exercise3_PE2 import (sum_even_fibonacci)

def test_exercise3() -> None:
    assert 4_613_732 == sum_even_fibonacci(4_000_000)