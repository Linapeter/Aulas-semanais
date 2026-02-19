from exercises.exercise9_PE5 import evenly_divisible

def test_exercise9() -> None:
    assert evenly_divisible(10) == 2_520
    assert evenly_divisible(20) == 232_792_560