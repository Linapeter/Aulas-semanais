def is_paired(text: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack: list[str] = []

    for ch in text:
        if ch in pairs.values():  # se for abertura
            stack.append(ch)
        elif ch in pairs:         # se for fechamento
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0
