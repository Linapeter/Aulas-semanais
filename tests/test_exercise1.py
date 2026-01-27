from python.exercise1_PE1 import multiples_3_and_5

def test_exercise1() -> None:
    assert 23 == multiples_3_and_5(10), "Test failed the example test"
    assert 233_168 == multiples_3_and_5(1_000), "Test failed to produce the expected result"