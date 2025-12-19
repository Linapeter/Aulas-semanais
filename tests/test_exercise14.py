from exercises.exercise14_MatchingBrackets import is_paired


def test_is_paired_cases() -> None:
    cases = [
        ("[]", True),
        ("", True),
        ("[[", False),
        ("}{", False),
        ("{]", False),
        ("{ }", True),
        ("{[])", False),
        ("{[]}", True),
        ("{}[]", True),
        ("([{}({}[])])", True),
        ("{[)][]}", False),
        ("([{])", False),
        ("[({]})", False),
        ("[({}])", False),
        ("{}[", False),
        ("[]]", False),
        (")()", False),
        ("{)()", False),
        ("(((185 + 223.85) * 15) - 543)/2", True),
        (
            "\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ "
            "\\mathrm{e}^{x} &... x^2 \\end{array}\\right)",
            True,
        ),
    ]

    for text, expected in cases:
        assert is_paired(text) == expected, f"Failed matching brackets to the text {text}"
