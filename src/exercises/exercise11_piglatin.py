# Pig Latin
# 1) If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
# 2) If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
# 3) If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
# 4) If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.


def translate(phrase: str) -> str:
    """
    Translate a phrase into Pig Latin.

    The phrase is split into words, eacharacter word is translated individually
    according to Pig Latin rules, and the results are joined back together.

    Parameters
    ----------
    phrase : str
        A string containing one or more words separated by spaces.

    Returns
    -------
    str
        The translated phrase in Pig Latin.
    """
    return " ".join(translate_word(word) for word in phrase.split())


def translate_word(word: str) -> str:
    """
    Translate a single word into Pig Latin.

    Pig Latin rules applied:
    1. If the word begins with a vowel, or starts with "xr" or "yt",
       append "ay" to the end.
    2. If the word begins with one or more consonants, move the consonant
       cluster to the end and append "ay".
    3. If the word starts with zero or more consonants followed by "qu",
       move the consonants and the "qu" together to the end, then append "ay".
    4. If the word starts with one or more consonants followed by "y",
       move the consonants preceding the "y" to the end, then append "ay".

    Parameters
    ----------
    word : str
        A single word to be translated.

    Returns
    -------
    str
        The word translated into Pig Latin.
    """
    vowels = {"a", "e", "i", "o", "u"}

    if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
        return word + "ay"

    i = 0
    while i < len(word):
        character = word[i]
        if character in vowels:
            break
        if character == "y" and i > 0:
            break
        if character == "q" and i + 1 < len(word) and word[i + 1] == "u":
            i += 2
            continue
        i += 1

    return word[i:] + word[:i] + "ay"
