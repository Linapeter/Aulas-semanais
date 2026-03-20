# Dominoes

# Introduction
# In Toyland, the trains are always busy delivering treasures across the city,
# from shiny marbles to rare building blocks.
# The tracks they run on are made of colorful domino-shaped pieces, each marked with two numbers.
# For the trains to move, the dominoes must form a perfect chain where the numbers match.

# Today, an urgent delivery of rare toys is on hold. You've been handed a set of track pieces to inspect.
# If they can form a continuous chain, the train will be on its way, bringing smiles across Toyland.
# If not, the set will be discarded, and another will be tried.

# The toys are counting on you to solve this puzzle.
# Will the dominoes connect the tracks and send the train rolling, or will the set be left behind?

# Instructions
# Make a chain of dominoes.

# Compute a way to order a given set of domino stones so that they form a correct domino chain.
# In the chain, the dots on one half of a stone must match the dots on the neighboring half of an adjacent stone.
# Additionally, the dots on the halves of the stones without neighbors
# (the first and last stone) must match each other.

# For example given the stones [2|1], [2|3] and [1|3] you should compute something like
# [1|2] [2|3] [3|1] or [3|2] [2|1] [1|3] or [1|3] [3|2] [2|1] etc,
# where the first and last numbers are the same.

# For stones [1|2], [4|1] and [2|3] the resulting chain is not valid:
# [4|1] [1|2] [2|3]'s first and last numbers are not the same. 4 != 3

# Some test cases may use duplicate stones in a chain solution,
# assume that multiple Domino sets are being used.


from typing import Iterator


class Dominoes:
    """
    Represents a collection of domino pieces and provides functionality
    to determine whether they can be arranged into a closed domino chain.
    """

    def __init__(
        self,
        pieces: list[tuple[int, int]],
    ) -> None:
        """
        Initialize a Dominoes object.

        Args:
            pieces: A list of domino pieces, where each piece is represented
                as a tuple of two integers (left_value, right_value).
        """
        self.pieces = pieces

    def __repr__(self) -> str:
        """
        Return a string representation of the domino pieces.

        Each piece is formatted as [a|b].

        Returns:
            A string showing all domino pieces in sequence.
        """
        return "".join(f"[{piece[0]}|{piece[1]}] " for piece in self.pieces)

    def get_chain(
        self,
        pieces: list[tuple[int, int]],
        chain: list[tuple[int, int]],
    ) -> Iterator[list[tuple[int, int]]]:
        """
        Recursively explores all possible combinations of dominoes to find a valid chain.

        This method uses a backtracking approach. It tries to append each available
        piece (and its reverse) to the current chain, ensuring the connecting
        numbers match. A chain is only yielded if it uses all pieces and forms
        a closed loop (the very first number matches the very last number).

        Args:
            pieces: A list of domino pieces (tuples) remaining to be placed.
            chain: The current sequence of dominoes already connected.

        Yields:
            Iterator[list[tuple[int, int]]]: A valid closed domino chain where
                all pieces are used and the ends match.
        """
        if not pieces:
            if chain and chain[0][0] == chain[-1][1]:
                yield chain
            return

        for index, piece in enumerate(pieces):
            rest_pieces: list[tuple[int, int]] = pieces[:index] + pieces[index + 1 :]
            options = [piece] if piece[0] == piece[1] else [piece, (piece[1], piece[0])]

            for oriented_piece in options:
                if not chain:
                    yield from self.get_chain(rest_pieces, [oriented_piece])
                else:
                    if oriented_piece[0] == chain[-1][1]:
                        yield from self.get_chain(rest_pieces, chain + [oriented_piece])

    def can_chain(self) -> list[tuple[int, int]]:
        """Determines if the collection of dominoes can form a valid closed chain.

        The method handles edge cases (empty list, single piece) and triggers
        the recursive search. It attempts to retrieve the first valid solution
        found by the generator.

        Returns:
            list[tuple[int, int]]: The first valid domino chain found.

        Raises:
            ValueError: If no valid closed chain can be formed with the given pieces.
        """
        if not self.pieces:
            return []

        if len(self.pieces) == 1:
            if self.pieces[0][0] == self.pieces[0][1]:
                return self.pieces
            raise ValueError("Cannot")

        try:
            return next(self.get_chain(self.pieces, []))
        except StopIteration:
            raise ValueError("Cannot")
