from exercises.exercise29 import longest_collatz_sequence

def test_exercise29() -> None:
    assert 837_799 == longest_collatz_sequence(1_000_000)