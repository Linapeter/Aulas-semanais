# Problem 18

# Maximum Path Sum I

# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23

#               3
#              7 4
#             2 4 6
#            8 5 9 3

# That is, 3+7+4+9 = 23

# Find the maximum total from top to bottom of the triangle below:

#                                75
#                              95 64
#                            17 47 82
#                          18 35 87 10
#                        20 04 82 47 65
#                      19 01 23 75 03 34
#                    88 02 77 73 07 63 67
#                  99 65 04 28 06 16 70 92
#                41 41 26 56 83 40 80 70 33
#              41 48 72 33 47 32 37 16 94 29
#            53 71 44 65 25 43 91 52 97 51 14
#          70 11 33 28 77 73 17 78 39 68 17 57
#        91 71 52 38 17 14 91 43 58 50 27 29 48
#      63 66 04 68 89 53 67 30 73 16 69 87 40 31
#    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

from typing import Callable


def parse_triangle(func: Callable[[list[list[int]]], int]) -> Callable[[str], int]:
    """
    Decorator that converts a triangle represented as a string into a
    list of integer rows before calling the decorated function.

    The decorated function must accept a triangle already parsed as
    `list[list[int]]`. This decorator allows the public interface to
    receive a multiline string, where each line represents a row of
    integers separated by spaces.

    The parsing process:
        - Strips leading/trailing whitespace
        - Splits the string by lines
        - Converts each value to an integer

    Args:
        func (Callable[[list[list[int]]], int]):
            A function that computes a result from a parsed numeric triangle.

    Returns:
        Callable[[str], int]:
            A new function that accepts a triangle as a string and returns
            the result produced by the decorated function.

    Example:
        >>> @parse_triangle
        ... def max_sum(lines: list[list[int]]) -> int:
        ...     return sum(lines[0])
        ...
        >>> triangle = "1\\n2 3\\n4 5 6"
        >>> max_sum(triangle)
        1
    """

    def wrapper(triangle: str) -> int:
        lines = [list(map(int, line.split())) for line in triangle.strip().splitlines()]
        return func(lines)

    return wrapper


@parse_triangle
def maximum_path_sum(lines: list[list[int]]) -> int:
    """Computes the maximum path sum in a numeric triangle.

    The triangle is given as a string with one row per line and integers
    separated by spaces. The function applies a bottom-up dynamic
    programming approach: starting from the second-to-last row, each element
    is replaced by its value plus the maximum of its two children in the row
    below. The top element becomes the maximum total from top to bottom.

    Args:
        triangle (str):
            A triangle represented as a multiline string, where each line
            contains integers separated by spaces. Example:
                "3\n7 4\n2 4 6\n8 5 9 3"

    Returns:
        int: The maximum path sum from the top to the bottom of the triangle.

    Example:
        >>> t =   3
                 7 4
                2 4 6
               8 5 9 3

        >>> maximum_path_sum(t)
        23
    """

    for line in range(len(lines) - 1, 0, -1):

        for index in range(0, len(lines[line - 1])):

            right = lines[line][index]
            left = lines[line][index + 1]

            lines[line - 1][index] += max(right, left)

    return lines[0][0]
