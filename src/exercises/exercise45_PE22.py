# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3+15+12+9+14 = 53, is the th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?


def names_scores(names: list[str]) -> int:
    """
    Calculate the total of all name scores from a list of names.

    Each name score is defined as:
        alphabetical value of the name * its position in the sorted list.

    - The alphabetical value of a name is the sum of its letters' values,
      where A=1, B=2, ..., Z=26.
    - The position is the 1-based index of the name after sorting the list
      in alphabetical order.

    Args:
        names (list[str]): A list of names (unsorted). Each name should be
                           provided as an uppercase string without quotes.

    Returns:
        int: The total sum of all name scores.

    Example:
        >>> names_scores(["COLIN", "ALEX", "BOB"])
        159
        # Sorted list: ["ALEX", "BOB", "COLIN"]
        # ALEX = 1+12+5+24 = 42, position 1 → 42*1 = 42
        # BOB = 2+15+2 = 19, position 2 → 19*2 = 38
        # COLIN = 3+15+12+9+14 = 53, position 3 → 53*3 = 159
        # Total = 42 + 38 + 159 = 239
    """
    names.sort()
    score = 0

    for position, name in enumerate(names, start=1):
        name_value = sum((ord(character) - 64) for character in name)
        score += name_value * (position)

    return score
