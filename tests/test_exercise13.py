from exercises.exercise13_PE7 import prime_in_position


def test_exercise13() -> None:
    assert prime_in_position(6) == 13
    assert prime_in_position(10_001) == 104_743
