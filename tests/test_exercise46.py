from exercises.exercise46_Dominoes import Dominoes

def test_simple_chain() -> None:
    dominoes = Dominoes([(1, 2), (2, 3), (3, 1), (3, 3)])
    assert [(2, 1), (1, 3), (3, 3), (3, 2)] == dominoes.can_chain()