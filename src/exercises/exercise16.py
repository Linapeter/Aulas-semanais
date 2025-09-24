
class Diamonds:
    alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, letter: str) -> None:
        self.letter = letter
        self.position: int = self.alphabet.find(self.letter)

    def spaces_in(self, idx: int) -> str:  # numeros impares
        return " " * (2 * idx - 1)

    def spaces_out(self, idx: int) -> str:
        return " " * (self.position - idx)

    def rows(self) -> list[str]:
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
