from functools import reduce


def translateROT(value: str, key: int, alphabet: str) -> list[str]:
    cipher = alphabet[key:] + alphabet[:key]
    translation: list[str] = []
    position = [
        idx
        for idx, letter in enumerate(alphabet.upper() if value.isupper() is True else alphabet)
        if letter == value
    ]

    for id in position:
        translation.append(cipher[id].upper() if value.isupper() is True else cipher[id])

    return translation

def rotate(text: str, key: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translation: list[str] = []

    for value in text:
        if value not in alphabet:
            translation.append(value)
        if value in alphabet:
            translation += translateROT(value, key, alphabet)

    return reduce(lambda x, y: x + y, translation)

