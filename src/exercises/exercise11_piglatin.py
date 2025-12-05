# Pig Latin
# 1) If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
# 2) If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
# 3) If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
# 4) If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.


def translate(phrase: str) -> str:
    return " ".join(translate_word(word) for word in phrase.split())


def translate_word(word: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}

    if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
        return word + "ay"

    i = 0
    while i < len(word):
        ch = word[i]
        if ch in vowels:
            break
        if ch == "y" and i > 0:
            break
        if ch == "q" and i + 1 < len(word) and word[i + 1] == "u":
            i += 2
            continue
        i += 1

    return word[i:] + word[:i] + "ay"
