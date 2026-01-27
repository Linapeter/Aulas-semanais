import pytest

from python.exercise11_piglatin import translate


@pytest.mark.parametrize(
    "text, expected",
    [
        ("apple", "appleay"),
        ("ear", "earay"),
        ("igloo", "iglooay"),
        ("object", "objectay"),
        ("under", "underay"),
        ("equal", "equalay"),
        ("pig", "igpay"),
        ("koala", "oalakay"),
        ("xenon", "enonxay"),
        ("qat", "atqay"),
        ("liquid", "iquidlay"),
        ("chair", "airchay"),
        ("queen", "eenquay"),
        ("square", "aresquay"),
        ("therapy", "erapythay"),
        ("thrush", "ushthray"),
        ("school", "oolschay"),
        ("yttria", "yttriaay"),
        ("xray", "xrayay"),
        ("yellow", "ellowyay"),
        ("rhythm", "ythmrhay"),
        ("my", "ymay"),
        ("quick fast run", "ickquay astfay unray"),
    ],
)
def test_translate_to_pig_latin(text: str, expected: str) -> None:
    """
    It should correctly translate words and phrases into Pig Latin
    following vowel and consonant cluster rules.
    """
    assert (
        translate(text) == expected
    ), f"Failed on translate the text {text} to pig latin. Expected: {expected}"
