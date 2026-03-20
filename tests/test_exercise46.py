from pytest import raises

from exercises.exercise46_Dominoes import Dominoes

Domino = tuple[int, int]
Chain = list[Domino]


def normalize_dominoes(dominoes: Chain) -> Chain:
    return sorted((a, b) if a <= b else (b, a) for a, b in dominoes)


def assert_same_dominoes(input_dominoes: Chain, output_chain: Chain) -> None:
    msg = (
        "Dominoes used in the output must be the same " "as the ones given in the input"
    )
    assert normalize_dominoes(input_dominoes) == normalize_dominoes(output_chain), msg


def assert_consecutive_dominoes_match(output_chain: Chain) -> None:
    for i in range(len(output_chain) - 1):
        msg = (
            f"In chain {output_chain}, right end of domino {i} ({output_chain[i]}) "
            f"and left end of domino {i+1} ({output_chain[i+1]}) must match"
        )
        assert output_chain[i][1] == output_chain[i + 1][0], msg


def assert_dominoes_at_ends_match(output_chain: Chain) -> None:
    msg = (
        f"In chain {output_chain}, left end of first domino ({output_chain[0]}) "
        f"and right end of last domino ({output_chain[-1]}) must match"
    )
    assert output_chain[0][0] == output_chain[-1][1], msg


def assert_correct_chain(input_dominoes: Chain, output_chain: Chain | None) -> None:
    msg = f"There should be a chain for {input_dominoes}"
    assert output_chain is not None, msg

    assert_same_dominoes(input_dominoes, output_chain)

    if not any(output_chain):
        return

    assert_consecutive_dominoes_match(output_chain)
    assert_dominoes_at_ends_match(output_chain)


def refute_correct_chain(input_dominoes: Chain) -> None:
    dominoes = Dominoes(input_dominoes)
    with raises(ValueError, match="Cannot"):
        dominoes.can_chain()


def test_empty_input_empty_output() -> None:
    input_dominoes: Chain = []
    output_chain = Dominoes(input_dominoes).can_chain()
    assert_correct_chain(input_dominoes, output_chain)


def test_singleton_input_singleton_output() -> None:
    input_dominoes: Chain = [(1, 1)]
    output_chain = Dominoes(input_dominoes).can_chain()
    assert_correct_chain(input_dominoes, output_chain)


def test_singleton_that_cant_be_chained() -> None:
    input_dominoes: Chain = [(1, 2)]
    refute_correct_chain(input_dominoes)


def test_three_elements() -> None:
    input_dominoes: Chain = [(1, 2), (3, 1), (2, 3)]
    output_chain = Dominoes(input_dominoes).can_chain()
    assert_correct_chain(input_dominoes, output_chain)


def test_can_reverse_dominoes() -> None:
    input_dominoes: Chain = [(1, 2), (1, 3), (2, 3)]
    output_chain = Dominoes(input_dominoes).can_chain()
    assert_correct_chain(input_dominoes, output_chain)


def test_cant_be_chained() -> None:
    input_dominoes: Chain = [(1, 2), (4, 1), (2, 3)]
    refute_correct_chain(input_dominoes)


def test_disconnected_simple() -> None:
    input_dominoes: Chain = [(1, 1), (2, 2)]
    refute_correct_chain(input_dominoes)


def test_disconnected_double_loop() -> None:
    input_dominoes: Chain = [(1, 2), (2, 1), (3, 4), (4, 3)]
    refute_correct_chain(input_dominoes)


def test_disconnected_single_isolated() -> None:
    input_dominoes: Chain = [(1, 2), (2, 3), (3, 1), (4, 4)]
    refute_correct_chain(input_dominoes)


def test_need_backtrack() -> None:
    input_dominoes: Chain = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
    output_chain = Dominoes(input_dominoes).can_chain()
    assert_correct_chain(input_dominoes, output_chain)


def test_separate_loops() -> None:
    input_dominoes: Chain = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
    output_chain = Dominoes(input_dominoes).can_chain()
    assert_correct_chain(input_dominoes, output_chain)


def test_nine_elements() -> None:
    input_dominoes: Chain = [
        (1, 2),
        (5, 3),
        (3, 1),
        (1, 2),
        (2, 4),
        (1, 6),
        (2, 3),
        (3, 4),
        (5, 6),
    ]
    output_chain = Dominoes(input_dominoes).can_chain()
    assert_correct_chain(input_dominoes, output_chain)


def test_separate_three_domino_loops() -> None:
    input_dominoes: Chain = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
    refute_correct_chain(input_dominoes)
