from functools import reduce


def translateROT(value: str, key: int, alphabet: str) -> list[str]:
    cipher = alphabet[key:] + alphabet[:key]
    translation: list[str] = []
    if value.isupper():
        for idx, letter in enumerate(alphabet.upper()):
            if letter == value:
                translation.append(cipher[idx].upper())
    if value.islower():
        for idx, letter in enumerate(alphabet):
            if letter == value:
                translation.append(cipher[idx])

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

print(rotate("O",5))
print(rotate("n",5))
