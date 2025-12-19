class Diamonds:
    """
    Generate a diamond pattern using uppercase letters.

    The diamond starts with 'A' at the top, expands line by line until
    the given letter is reached, and then mirrors back to 'A'.
    """

    alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(
        self,
        letter: str,
    ) -> None:
        """
        Initialize the diamond with a target letter.

        Parameters
        ----------
        letter : str
            The uppercase letter that defines the widest point
            of the diamond.
        """
        self.letter = letter
        self.position: int = self.alphabet.find(self.letter)

    def spaces_in(
        self,
        idx: int,
    ) -> str:  # numeros impares
        """
        Return the inner spaces between duplicated letters.

        The number of inner spaces grows as odd numbers:
        1, 3, 5, ...

        Parameters
        ----------
        idx : int
            Index of the current letter in the alphabet.

        Returns
        -------
        str
            A string of spaces used between letters.
        """
        return " " * (2 * idx - 1)

    def spaces_out(
        self,
        idx: int,
    ) -> str:
        """
        Return the outer spaces before and after letters.

        These spaces center each row according to the position
        of the target letter.

        Parameters
        ----------
        idx : int
            Index of the current letter in the alphabet.

        Returns
        -------
        str
            A string of spaces used for padding.
        """
        return " " * (self.position - idx)

    def rows(self) -> list[str]:
        """
        Build the diamond row by row.

        The diamond is constructed by:
        - Expanding from 'A' up to the target letter.
        - Mirroring the rows back down to 'A'.

        Returns
        -------
        list[str]
            A list of strings, each representing one row of the diamond.
        """
        lines: list[str] = []

        for letter_up in range(self.position + 1):
            if not letter_up:
                lines.append(self.spaces_out(0) + "A" + self.spaces_out(0))
            else:
                lines.append(
                    self.spaces_out(letter_up)
                    + self.alphabet[letter_up]
                    + self.spaces_in(letter_up)
                    + self.alphabet[letter_up]
                    + self.spaces_out(letter_up)
                )

        for lett_down in range(self.position - 1, -1, -1):
            if not lett_down:
                lines.append(self.spaces_out(0) + "A" + self.spaces_out(0))
            else:
                lines.append(
                    self.spaces_out(lett_down)
                    + self.alphabet[lett_down]
                    + self.spaces_in(lett_down)
                    + self.alphabet[lett_down]
                    + self.spaces_out(lett_down)
                )

        return lines
