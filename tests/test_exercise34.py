import re

from exercises.exercise34_VigenèreCipher import Cipher


def test_can_encode_random_key() -> None:
    cipher = Cipher()
    plaintext = "aaaaaaaaaa"
    assert (
        cipher.encode(plaintext) == cipher.key[0 : len(plaintext)]
    ), f"Failed encoding the text {plaintext} with random key (first test)"


def test_can_decode_random_key() -> None:
    cipher = Cipher()
    assert (
        cipher.decode(cipher.key[0 : len("aaaaaaaaaa")]) == "aaaaaaaaaa"
    ), "Failed decoding the text above with random key (second test)"


def test_is_reversible_random_key() -> None:
    cipher = Cipher()
    plaintext = "abcdefghij"
    assert (
        cipher.decode(cipher.encode(plaintext)) == plaintext
    ), f"Failed encoding the text {plaintext} with random key (third test)"


def test_key_is_made_only_of_lowercase_letters() -> None:
    assert re.match("^[a-z]+$", Cipher().key) is not None, "Failed on fourth test"


def test_can_encode() -> None:
    cipher = Cipher("abcdefghij")
    plaintext = "aaaaaaaaaa"
    assert (
        cipher.encode(plaintext) == cipher.key
    ), f"Failed encoding the text {plaintext} with the key abcdefghij"


def test_can_decode() -> None:
    cipher = Cipher("abcdefghij")
    assert (
        cipher.decode(cipher.key) == "aaaaaaaaaa"
    ), "Failed decoding the text above with the key abcdefghij"


def test_is_reversible() -> None:
    cipher = Cipher("abcdefghij")
    plaintext = "abcdefghij"
    assert (
        cipher.decode(cipher.encode(plaintext)) == plaintext
    ), f"Failed encoding the text {plaintext} with the key abcdefghij"


def test_can_double_shift_encode() -> None:
    cipher = Cipher("iamapandabear")
    plaintext = "iamapandabear"
    assert (
        cipher.encode(plaintext) == "qayaeaagaciai"
    ), f"Failed encoding the text {plaintext} with the key iamapandabear"


def test_can_wrap_on_encode() -> None:
    cipher = Cipher("abcdefghij")
    plaintext = "zzzzzzzzzz"
    assert (
        cipher.encode(plaintext) == "zabcdefghi"
    ), f"Failed encoding the text {plaintext} with the key abcdefghij"


def test_can_wrap_on_decode() -> None:
    cipher = Cipher("abcdefghij")
    assert (
        cipher.decode("zabcdefghi") == "zzzzzzzzzz"
    ), "Failed decoding the text zabcdefghi with the key abcdefghij"


def test_can_encode_messages_longer_than_key() -> None:
    cipher = Cipher("abc")
    plaintext = "iamapandabear"
    assert (
        cipher.encode(plaintext) == "iboaqcnecbfcr"
    ), f"Failed encoding the text {plaintext} with the key abc"


def test_can_decode_messages_longer_than_key() -> None:
    cipher = Cipher("abc")
    assert (
        cipher.decode("iboaqcnecbfcr") == "iamapandabear"
    ), "Failed decoding the text iboaqcnecbfcr with the key abc"
