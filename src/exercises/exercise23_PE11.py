# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20x20 grid?

from numpy import ndarray, array, diag, fliplr, prod


def greatest_product_horizontal(
    grid: ndarray, dimension: int, adjacent_numbers: int
) -> int:
    largest_product: int = 0
    for row in range(dimension):
        for column in range(dimension - adjacent_numbers + 1):
            product = int(prod(grid[row, column : column + adjacent_numbers]))
            largest_product = max(largest_product, product)
    return largest_product


def greatest_product_diagonal(
    grid: ndarray,
    dimension: int,
    adjacent_numbers: int,
) -> int:
    largest_product = 0
    for index in range(-dimension + 1, dimension):
        diagonal = diag(grid, k=index)
        for item in range(len(diagonal) - adjacent_numbers + 1):
            product = int(prod(diagonal[item : item + adjacent_numbers]))
            largest_product = max(largest_product, product)
    return largest_product


def grid_largest_product(grid: str, dimension: int, adjacent_numbers: int) -> int:
    """Calculates the largest product of adjacent numbers in a square grid.

    This function takes a string of integers separated by spaces and reshapes it
    into a `dimension x dimension` matrix. It then searches horizontally, vertically,
    and diagonally (both downward and upward) for the maximum product of `adjacent_numbers` consecutive values.

    Args:
        grid (str): A string containing all the grid numbers separated by spaces.
        dimension (int): The number of rows and columns in the square matrix (e.g., `20` for a 20x20 grid).
        adjacent_numbers (int): The number of consecutive numbers to consider when calculating the product.

    Returns:
        int: The largest product of `adjacent_numbers` consecutive numbers found in any direction.

    Notes:
        - The function considers products in four directions:
            * Horizontal (left to right)
            * Vertical (top to bottom)
            * Diagonal (down-right)
            * Diagonal (up-right)
        - If `adjacent_numbers` is greater than `dimension`, the result will be 0.
    """
    numbers = list(map(int, grid.split()))
    mtx = array(numbers).reshape((dimension, dimension))

    lines = greatest_product_horizontal(mtx, dimension, adjacent_numbers)
    columns = greatest_product_horizontal(mtx.T, dimension, adjacent_numbers)
    diagonal_down = greatest_product_diagonal(mtx, dimension, adjacent_numbers)
    diagonal_up = greatest_product_diagonal(fliplr(mtx), dimension, adjacent_numbers)
    return max(lines, columns, diagonal_up, diagonal_down)
