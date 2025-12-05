from exercises.exercise1_PE1 import multiples_3_and_5

def test_exercise1() -> None:
    assert 23 == multiples_3_and_5(10)
    assert 233168 == multiples_3_and_5(1_000)