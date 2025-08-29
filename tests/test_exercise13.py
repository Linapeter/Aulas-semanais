from exercises.exercise13 import prime_in_position


def test_exercise13() -> None:
    assert prime_in_position(6) == 13
    assert prime_in_position(10_001) == 104_743

    assert prime_in_position(1) == 2
    assert prime_in_position(2) == 3
    assert prime_in_position(3) == 5
