from exercises.exercise12_rotateROT import rotate


def test_rotate_a_by_0_same_output_as_input() -> None:
    assert rotate("a", 0) == "a"


def test_rotate_a_by_1() -> None:
    assert rotate("a", 1) == "b"


def test_rotate_a_by_26_same_output_as_input() -> None:
    assert rotate("a", 26) == "a"


def test_rotate_m_by_13() -> None:
    assert rotate("m", 13) == "z"


def test_rotate_n_by_13_with_wrap_around_alphabet() -> None:
    assert rotate("n", 13) == "a"


def test_rotate_capital_letters() -> None:
    assert rotate("OMG", 5) == "TRL"


def test_rotate_spaces() -> None:
    assert rotate("O M G", 5) == "T R L"


def test_rotate_numbers() -> None:
    assert rotate("Testing 1 2 3 testing", 4) == "Xiwxmrk 1 2 3 xiwxmrk"


def test_rotate_punctuation() -> None:
    assert rotate("Let's eat, Grandma!", 21) == "Gzo'n zvo, Bmviyhv!"


def test_rotate_all_letters() -> None:
    assert (
        rotate("The quick brown fox jumps over the lazy dog.", 13)
        == "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
    )
