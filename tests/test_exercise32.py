import pytest

from exercises.exercise32_Hamming import distance


@pytest.mark.parametrize(
    "text_a, text_b, expected",
    [
        ("", "", 0),
        ("A", "A", 0),
        ("G", "T", 1),
    ],
    ids=[
        "both empty",
        "same single letter",
        "different single letters",
    ],
)
def test_single_letters_strands(
    text_a: str,
    text_b: str,
    expected: int,
) -> None:
    result: int = distance(text_a, text_b)
    assert result == expected, (
        f"distance({text_a!r}, {text_b!r}) returned {result}, "
        f"expected {expected}"
    )


@pytest.mark.parametrize(
    "text_a, text_b, expected",
    [
        ("GGACTGAAATCTG", "GGACTGAAATCTG", 0),
        ("GGACGGATTCTG", "AGGACGGATTCT", 9),
    ],
    ids=[
        "identical long strands",
        "completely different long strands",
    ],
)
def test_long_distance(
    text_a: str,
    text_b: str,
    expected: int,
) -> None:
    result: int = distance(text_a, text_b)
    assert result == expected, (
        f"distance({text_a!r}, {text_b!r}) returned {result}, "
        f"expected {expected}"
    )


@pytest.mark.parametrize(
    "text_a, text_b, error_message",
    [
        ("AATG", "AAA", "Strands must be of equal length."),
        ("ATA", "AGTG", "Strands must be of equal length."),
        ("", "G", "Strands must be of equal length."),
        ("G", "", "Strands must be of equal length."),
    ],
    ids=[
        "first longer than second",
        "second longer than first",
        "first empty second non-empty",
        "first non-empty second empty",
    ],
)
def test_error_message(
    text_a: str,
    text_b: str,
    error_message: str,
) -> None:
    with pytest.raises(ValueError, match=error_message):
        distance(text_a, text_b)
