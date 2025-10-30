# Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.

# For example, the string "49142" has the following 3-digit series:

# "491"
# "914"
# "142"
# And the following 4-digit series:

# "4914"
# "9142"
# And if you ask for a 6-digit series from a 5-digit string, you deserve whatever you get.

# Note that these series are only required to occupy adjacent positions in the input; the digits need not be numerically consecutive.


def slice_series(
    series: str,
    length: int,
) -> list[str]:
    """Return all possible consecutive slices of a given length from the input string.

    This function extracts substrings of the specified length from the given
    string `series`, moving one character at a time. For example, slicing the
    string `"12345"` with length `3` returns `["123", "234", "345"]`.

    Args:
        series (str): The input string to be sliced.
        length (int): The length of each slice.

    Raises:
        ValueError: If `length` is zero.
        ValueError: If `length` is negative.
        ValueError: If `series` is empty.
        ValueError: If `length` is greater than the length of `series`.

    Returns:
        list[str]: A list of substrings of length `length` extracted from `series`.
    """
    if not length:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[i : i + length] for i in range(0, len(series) - length + 1)]
