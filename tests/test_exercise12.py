from python.exercise12_rotateROT import rotate

import pytest


@pytest.mark.parametrize(
    "text, shift, expected",
    [
        ("a", 0, "a"),
        ("a", 1, "b"),
        ("a", 26, "a"),
        ("m", 13, "z"),
        ("n", 13, "a"),
        ("OMG", 5, "TRL"),
        ("O M G", 5, "T R L"),
        ("Testing 1 2 3 testing", 4, "Xiwxmrk 1 2 3 xiwxmrk"),
        ("Let's eat, Grandma!", 21, "Gzo'n zvo, Bmviyhv!"),
        (
            "The quick brown fox jumps over the lazy dog.",
            13,
            "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
        ),
    ],
    ids=[
        "rotate by 0 (identity)",
        "rotate single letter",
        "rotate by 26 (full alphabet)",
        "rotate mid alphabet",
        "rotate with wrap around",
        "rotate capital letters",
        "rotate spaces preserved",
        "rotate numbers preserved",
        "rotate punctuation preserved",
        "rotate full sentence (ROT13)",
    ],
)
def test_rotate(
    text: str,
    shift: int,
    expected: str,
) -> None:
    result: str = rotate(text, shift)
    assert result == expected, (
        f"rotate(text={text!r}, shift={shift}) returned {result!r}, "
        f"expected {expected!r}"
    )
