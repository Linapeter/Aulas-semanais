# Simple Cipher
# Create an implementation of the Vigenère cipher. The Vigenère cipher is a simple substitution cipher.

# é importante o número da letra [(a,0),(b,2), (c,3), (d,4), ...]
# key = abcd
# text = hello
# assim, h(7) + a(0) = h(7)
#        e(4) + b(1) = f(5)
#        l(11) + c(2) = n(13)
#        l(11) + d(3) = o(12)
#        o(14) + a(0) = o(13)

# se a key for menor que o texto vai repetindo o key do inicio


from random import choices


class Cipher:
    """A simple substitution cipher based on shifting letters using a key.
    The key acts as a repeating sequence of shifts, similar to the classical
    Vigenère cipher. Each character in the key determines how many positions
    a plaintext letter should be shifted in the alphabet.

    The cipher only supports lowercase alphabetic characters ('a'–'z').
    Any input text is converted to lowercase before encoding or decoding.

    Attributes:
        alphabet (str): The set of valid characters for encoding and decoding.
        key (str): The encryption key. If not provided, a random 100-letter
            key composed of lowercase alphabet letters is generated.
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, key: str = "") -> None:
        """
        Initializes the cipher with a provided key or generates a random one.

        If no key is provided, a random key of length 100 is generated using
        lowercase alphabet letters. The key is always stored in lowercase.

        Args:
            key (str, optional):
                A string used as the encryption/decryption key.
                If empty, a random 100-character key is generated.
        """
        self.key = "".join(choices(self.alphabet, k=100)) if not key else key.lower()
    # TODO __repr__

    def encode(self, text: str) -> str:
        """Encodes a plaintext string into ciphertext using the cipher's key.

        The key is repeated or truncated as necessary to match the length
        of the input text. Each character in the plaintext is shifted
        forward in the alphabet by an amount based on the corresponding
        character in the key.

        Non-alphabet characters are not supported and will cause an error.

        Args:
            text (str):
                The plaintext message to encode. Converted to lowercase.

        Returns:
            str:
                The encoded ciphertext string.
        """
        encoded = ""
        text = text.lower()

        if len(text) > len(self.key):
            right_key = (self.key * (len(text) // len(self.key) + 1))[: len(text)] # len(text) = 10 então key='abcabcabca'
        else:
            right_key = self.key[: len(text)]

        for letter_text, letter_key in zip(text, right_key):
            index_encoded = (
                self.alphabet.index(letter_text) + self.alphabet.index(letter_key)
            ) % 26
            encoded += self.alphabet[index_encoded]

        return encoded

    def decode(self, text: str) -> str:
        """Decodes a ciphertext string back into plaintext using the cipher's key.

        The key is repeated or truncated as needed to match the ciphertext
        length. Each character in the ciphertext is shifted backward in
        the alphabet by an amount determined by the corresponding character
        in the key.

        Args:
            text (str):
                The encoded ciphertext to decode. Converted to lowercase.

        Returns:
            str:
                The decoded plaintext string.
        """
        decoded = ""
        text = text.lower()

        if len(text) > len(self.key):
            right_key = (self.key * (len(text) // len(self.key) + 1))[: len(text)]
        else:
            right_key = self.key[: len(text)]

        for letter_text, letter_key in zip(text, right_key):
            index_decoded = (
                self.alphabet.index(letter_text) - self.alphabet.index(letter_key)
            ) % 26
            decoded += self.alphabet[index_decoded]

        return decoded
