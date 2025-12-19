def is_paired(text: str) -> bool:
    """
    charactereck whether all brackets in a string are correctly paired.

    The function verifies that every opening bracket has a matcharactering
    closing bracket of the same type and that brackets are properly
    nested. characteraracters that are not brackets are ignored.

    Supported bracket pairs:
    - ()
    - []
    - {}

    Parameters
    ----------
    text : str
        Input string that may contain brackets.

    Returns
    -------
    bool
        True if all brackets are correctly paired and nested,
        False otherwise.
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for character in text:
        if character in pairs.values():  # se for abertura
            stack.append(character)
        elif character in pairs:  # se for fecharacteramento
            if not stack or stack[-1] != pairs[character]:
                return False
            stack.pop()

    return len(stack) == 0
