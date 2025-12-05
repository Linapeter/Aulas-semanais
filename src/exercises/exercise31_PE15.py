# Project Euler
# Problem 15
# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# numa grade de 2 por 2, temos 4 passos: 2 pra direita e 2 pra baixo (2R 2D)
# permutação com repetição: 4! / (2! 2!)

# Assim, se for 3x3, temos 6 passos: 3 pra direita e 3 pra baixo (3R 3D)
# permutação com repetição: 6! / (3! 3!)

# n grid: 2n! / (n! n!)

from math import comb


def grid_routes(
    dimension: int,
) -> int:
    """This function return the number of routes that has a n-grid

    Args:
        dimension (int): dimension of the grid nxn

    Returns:
        int: number of routes
    """
    return int(comb(dimension * 2, dimension))
