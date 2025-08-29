# class matching_brackets:
#     pairs = {
#         "(": ")",
#         "[": "]",
#         "{": "}",
#     }

#     def __init__(self, text: str) -> None:
#         self.text = text

#     def is_paired(self) -> bool:
#         list_of_brackets: list[str] = []

#         for character in self.text:
#             if character in self.pairs:  # abre
#                 list_of_brackets.append(character)

#             if character in self.pairs.values():  # fecha
#                 if (
#                     list_of_brackets == []
#                     or self.pairs[list_of_brackets.pop()] != character
#                 ):  # não teve abertura ou o último da lista não fecha o par
#                     return False

#         return list_of_brackets == []  # True ou False se a lista estiver vazia ou não


def is_paired(text: str) -> bool:
    pairs = "()[]{}"
    acc = 0
    just = "".join(filter(lambda c: c in pairs, text))
    for i in just:
        while acc >= 0:
            if i in "([{":
                acc += 1
            if i in ")]}":
                acc -= 1
    if acc == 0:
        return True
    else:
        return False

print(is_paired("[({})"))
