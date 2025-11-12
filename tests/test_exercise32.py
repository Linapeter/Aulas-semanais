import pytest

from exercises.exercise32 import distance


@pytest.mark.parametrize(
    "text_a, text_b, expected",
    [
        ("", "", 0),
        ("A", "A", 0),
        ("G", "T", 1),
    ],
)
def test_single_letters_strands(
    text_a: str,
    text_b: str,
    expected: int,
) -> None:
    assert distance(text_a, text_b) == expected


@pytest.mark.parametrize(
    "text_a,text_b,expected",
    [
        ("GGACTGAAATCTG", "GGACTGAAATCTG", 0),
        ("GGACGGATTCTG", "AGGACGGATTCT", 9),
    ]
)

def test_long_distance(
    text_a: str,
    text_b: str,
    expected: int,
) -> None:
    assert distance(text_a, text_b) == expected


@pytest.mark.parametrize(
    "text_a,text_b,error_message",
    [
        ("AATG", "AAA", "Strands must be of equal length."),
        ("ATA", "AGTG", "Strands must be of equal length."),
        ("", "G", "Strands must be of equal length."),
        ("G", "", "Strands must be of equal length."),
    ]
)
def test_error_message(
    text_a: str,
    text_b: str,
    error_message: str,
) -> None:
    with pytest.raises(ValueError, match=error_message):
        distance(text_a, text_b)
