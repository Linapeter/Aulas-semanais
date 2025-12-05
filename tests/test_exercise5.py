from exercises.exercise5_PE3 import largest_prime


def test_exercise5() -> None:
    assert 31 == largest_prime(1395)
    assert 6857 == largest_prime(600_851_475_143)
