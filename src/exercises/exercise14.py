def is_paired(text: str) -> bool:
    brackets = {"(": 1, ")": -1, "[": 10, "]": -10, "{": 100, "}": -100}
    just_brackets = "".join(c for c in text if c in brackets)
    acc = 0
    for i in just_brackets:
        acc += brackets[i]

        if acc < 0:
            return False

        if acc % 10 != 0 and brackets[i] < 0 and abs(brackets[i]) != abs(acc % 10):
            return False

    return acc == 0
