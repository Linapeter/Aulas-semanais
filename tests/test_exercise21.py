
from exercises.exercise21 import sum_of_prime

def test_exercise21() -> None:
    assert 142_913_828_922 == sum_of_prime(2_000_000)