
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

class Dominoes:

    def __init__(self, pieces: list[tuple[int,int]]) -> None:
        self.pieces = pieces
        self.length = len(self.pieces)

    def __repr__(self) -> str:
        return "[|]"

    def swap(self, piece: tuple[int,int]) -> tuple[int,int]:
        """
        Swap the two elements of a 2 element tuple.
        Args:
            piece (tuple[int, int]): A tuple containing exactly two integers.
        Returns:
            tuple[int, int]: A new tuple with the elements swapped.
                            For example, (a, b) becomes (b, a).
        """
        left, right = piece
        return (right, left)

    def corner_pieces(self) -> list[tuple[int,int]]:

        for piece in range(self.length):
            for next in range(piece + 1, self.length):

                common = set(self.pieces[piece]) & set(self.pieces[next])
                if common: # intersection
                    common_value = common.pop()

                    if common_value == self.pieces[piece][1]:
                        self.pieces[piece] = self.swap(self.pieces[piece])

                    if common_value == self.pieces[next][0]:
                        self.pieces[next] = self.swap(self.pieces[next])

                    return [self.pieces[piece], self.pieces[next]]

        raise ValueError("Pieces don't match")

    def can_chain(self) -> list[tuple[int,int]]:
        corners = self.corner_pieces()

        self.pieces.remove(corners[0])
        self.pieces.remove(corners[1])

        chain = [corners[0]]

        while self.pieces:
            last_piece = chain[-1]

            for piece in self.pieces:
                if last_piece[1] in piece:
                    self.pieces.remove(piece)

                    if piece[0] != last_piece[1]:
                        piece = self.swap(piece)

                    chain.append(piece)
                    break
            else:
                raise ValueError("Cannot complete the chain")

        if chain[-1][1] != corners[1][0]:
            raise ValueError("Cannot complete the chain")

        chain.append(corners[1])

        return chain


