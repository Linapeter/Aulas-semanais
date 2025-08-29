from functools import reduce


def translateROT(
    value: str,
    key: int,
    alphabet: str,
) -> str:
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translation: list[str] = []

    for value in text:
        translation += translateROT(value, key, alphabet)

    return reduce(lambda x, y: x + y, translation)
