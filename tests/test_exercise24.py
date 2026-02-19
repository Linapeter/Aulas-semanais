from exercises.exercise24_Acronym import abbreviate
import pytest

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Portable Network Graphics", "PNG"),
        ("Ruby on Rails", "ROR"),
        ("First In, First Out", "FIFO"),
        ("GNU Image Manipulation Program", "GIMP"),
        ("Complementary metal-oxide semiconductor", "CMOS"),
        (
            "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me",
            "ROTFLSHTMDCOALM",
        ),
        ("Something - I made up from thin air", "SIMUFTA"),
        ("Halley's Comet", "HC"),
        ("The Road _Not_ Taken", "TRNT"),
    ],
    ids=[
        "basic phrase",
        "lowercase words",
        "punctuation",
        "all caps word",
        "hyphen without whitespace",
        "very long abbreviation",
        "consecutive delimiters",
        "apostrophes",
        "underscore emphasis",
    ],
)
def test_abbreviate(
    text: str,
    expected: str,
) -> None:
    result: str = abbreviate(text)
    assert result == expected, (
        f"abbreviate(text={text!r}) returned {result!r}, "
        f"expected {expected!r}"
    )