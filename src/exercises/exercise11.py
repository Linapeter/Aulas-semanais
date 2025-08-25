# Pig Latin
# 1) If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
# 2) If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
# 3) If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
# 4) If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

def translate(word:str) -> str:
    vowel = {"a","e","i","o","u"}
    if (word[0] in vowel) or (word[0:2]=="xr") or (word[0:2]=="yt"):
        word = word

    visit = 0
    if (word[0] not in vowel) and (word[0:2]!="xr") and (word[0:2]!="yt"):
        while visit < len(word) and (word[visit] not in vowel):
            if word[visit:visit+2] == "qu":
                visit += 1
            elif word[visit] == "y":
                break
            visit += 1

        word = word[visit:] + word[:visit]

    return word + "ay"
