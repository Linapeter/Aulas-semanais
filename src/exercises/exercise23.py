# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20x20 grid?

import numpy as np


def grid_largest_product(grid: str, dimension: int, adjacent_numbers: int) -> int:
    numbers = list(map(int, grid.split()))
    matrix = np.array(numbers).reshape((dimension, dimension))
    largest_product: int = 0

    for row in range(dimension):
        for column in range(dimension):

            if column + adjacent_numbers <= dimension:
                # horizontalmente
                horizontal = matrix[row, column : column + adjacent_numbers]
                product: int = np.prod(horizontal)
                largest_product = max(largest_product, product)

            if row + adjacent_numbers <= dimension:
                # verticalmente
                vertical = matrix[row : row + adjacent_numbers, column]
                product = np.prod(vertical)
                largest_product = max(largest_product, product)

            if (
                row + adjacent_numbers <= dimension
                and column + adjacent_numbers <= dimension
            ):
                # diagonal para baixo
                diag_down = [
                    matrix[row + i, column + i] for i in range(adjacent_numbers)
                ]
                product = np.prod(diag_down)
                largest_product = max(largest_product, product)

            if row - adjacent_numbers >= -1 and column + adjacent_numbers <= dimension:
                # diagonal para baixo
                diag_up = [matrix[row - i, column + i] for i in range(adjacent_numbers)]
                product = np.prod(diag_up)
                largest_product = max(largest_product, product)

    return largest_product
