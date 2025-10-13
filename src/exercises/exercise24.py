# Instructions
# Convert a phrase to its acronym.

# Techies love their TLA (Three Letter Acronyms)!

# Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).

# Punctuation is handled as follows: hyphens are word separators (like whitespace); all other punctuation can be removed from the input.

# For example:

# Input	Output
# As Soon As Possible	ASAP
# Liquid-crystal display	LCD
# Thank George It's Friday!	TGIF


def abbreviate(phrase: str) -> str:
    """Convert a phrase to its acronym.

    Args:
        phrase (str): a phrase to be abbreviated

    Returns:
        str: abbreviation
    """
    words = phrase

    if "-" in words:
        words = words.replace("-", " ")

    list_words = words.split()
    acronym = ""

    for word in list_words:
        word = word.strip(",_/?!@#$%&*()+[];:º~^")
        acronym += word[0]

    return acronym.upper()
