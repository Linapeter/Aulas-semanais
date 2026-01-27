# Hamming

# DNA cells

# Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they achieve by dividing into daughter cells. In fact, the average human body experiences about 10 quadrillion cell divisions in a lifetime!

# When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of DNA get encoded with the incorrect information. If we compare two strands of DNA and count the differences between them, we can see how many mistakes occurred. This is known as the "Hamming distance".

# The Hamming distance is useful in many areas of science, not just biology, so it's a nice phrase to be familiar with :)

# Instructions
# Calculate the Hamming distance between two DNA strands.

# We read DNA using the letters C, A, G and T. Two strands might look like this:

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^  ^ ^    ^^
# They have 7 differences, and therefore the Hamming distance is 7.

from typing import Callable, Iterable, Tuple


def zipped(
    func: Callable[[Iterable[Tuple[str, str]]], int],
) -> Callable[[str, str], int]:
    """
    Decorator that adapts a function operating on paired characters
    to accept two strings of equal length.

    The decorated function will:
    - Validate that both strings have the same length
    - Zip the strings into pairs
    - Pass the pairs to the original function
    """

    def wrapper(strand_a: str, strand_b: str) -> int:

        if len(strand_a) != len(strand_b):
            raise ValueError("Strands must be of equal length.")

        return func(zip(strand_a, strand_b))

    return wrapper


@zipped
def distance(
    strands: Iterable[Tuple[str, str]],
) -> int:  # distance = zipped(distance),
    # Então, ao chamar a função distance (com @zipped), ele primeiro zippa as strands que quero e chama como strands mesmo, isso se as len's forem iguais
    """
    Compute the Hamming distance between two DNA strands.

    Parameters
    ----------
    strands : Iterable[Tuple[str, str]]
        Paired characters from two DNA strands.

    Returns
    -------
    int
        Number of positions at which the corresponding symbols differ.
    """
    return sum(strand_a != strand_b for strand_a, strand_b in strands)


# def distance(
#     strand_a: str,
#     strand_b: str,
# ) -> int:
#     """This function receives two DNA strands of the same length and calculates the Hamming distance.

#     Args:
#         strand_a (str): first DNA strand
#         strand_b (str): second DNA strand

#     Raises:
#         ValueError: If the lengths of the strands are not equal.

#     Returns:
#         int: The Hamming distance
#     """

#     if len(strand_a) != len(strand_b):
#         raise ValueError("Strands must be of equal length.")

#     return sum(strand_a != strand_b for strand_a, strand_b in zip(strand_a, strand_b))
