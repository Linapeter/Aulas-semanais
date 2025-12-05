# Problem 17 - Number Letter Counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3+3+5+4+4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
# 23 letter and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

from exercises.exercise22_SpellOutNumbers import spell_our_numbers


def counting(
    number: int,
) -> int:
    """
    Return the number of letters in the English spelling of a given number.

    This function uses `spell_our_numbers` to generate the written-out form
    of the integer (e.g., 342 → "three hundred forty-two"), then removes
    spaces and hyphens and counts the remaining characters.

    According to the traditional rule used in Project Euler Problem 17,
    an additional 3 letters are added for the word "and" whenever:
      - the number is greater than 100, and
      - it is not a clean multiple of 100 (i.e., it has additional tens/units).

    Examples:
        counting(5) → 4                     # "five"
        counting(115) → 20                 # "one hundred and fifteen"
        counting(300) → 12                 # "three hundred" (no "and")

    Parameters
    ----------
    number : int
        The integer to convert and count letters from.

    Returns
    -------
    int
        The number of letters in the written-out form of the number.
    """
    length = len(spell_our_numbers(number).say().replace(" ", "").replace("-", ""))
    return length + 3 if (number > 100) and (number % 100 != 0) else length
    # "and"


def counting_until(
    limit: int,
) -> int:
    """
    Compute the total number of letters used when writing out all numbers
    from 1 up to the specified limit (inclusive).

    This function applies `counting()` to each integer in the range
    `[1, limit]` and returns the sum of all letter counts.

    Examples:
        counting_until(5)
            → counting(1) + ... + counting(5)
            → 3 + 3 + 5 + 4 + 4 = 19

    Parameters
    ----------
    limit : int
        The upper bound (inclusive) for the count.

    Returns
    -------
    int
        The sum of letter counts for all numbers from 1 to `limit`.
    """
    return sum(counting(number) for number in range(1, limit + 1))
