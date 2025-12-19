from functools import reduce


def translateROT(
    value: str,
    key: int,
    alphabet: str,
) -> str:
    """
    Apply a ROT (rotation) cipher to a single character.

    The function shifts alphabetic characters by a given key within the
    provided alphabet. Uppercase and lowercase letters are preserved.
    Non-alphabetic characters are returned unchanged.

    Parameters
    ----------
    value : str
        A single character to be translated.
    key : int
        Number of positions to rotate the character.
    alphabet : str
        The base alphabet used for the rotation (lowercase).

    Returns
    -------
    str
        The translated character after applying the ROT cipher.
    """
    cipher = alphabet[key:] + alphabet[:key]

    if value.isupper():
        for idx, letter in enumerate(alphabet.upper()):
            if letter == value:
                return cipher[idx].upper()

    if value.islower():
        for idx, letter in enumerate(alphabet):
            if letter == value:
                return cipher[idx]

    return value


def rotate(
    text: str,
    key: int,
) -> str:
    """
    Apply a ROT cipher to an entire string.

    Each character in the text is processed individually using the ROT
    cipher. Alphabetic characters are rotated by the given key, while
    non-alphabetic characters remain unchanged.

    Parameters
    ----------
    text : str
        The input text to be encrypted or decrypted.
    key : int
        Number of positions to rotate each alphabetic character.

    Returns
    -------
    str
        The transformed text after applying the ROT cipher.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translation: list[str] = []

    for value in text:
        translation += translateROT(value, key, alphabet)

    return reduce(lambda x, y: x + y, translation)
