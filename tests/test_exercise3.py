from exercises.exercise3 import (sum_even_fibonacci)

def test_exercise3() -> None:
    assert 4613732 == sum_even_fibonacci(4_000_000)