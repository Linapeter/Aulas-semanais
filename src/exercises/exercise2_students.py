# Exercise 2

# Students Class created to receive name and grade


class students:

    def __init__(self) -> None:
        self._dict_students: dict[str, int] = {}
        self._added: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        if name not in self._dict_students:
            self._dict_students[name] = grade
            self._added.append(True)
        else:
            self._added.append(False)

    def roster(self) -> list[str]:
        return [
            name
            for name, _ in sorted(
                self._dict_students.items(), key=lambda x: (x[1], x[0])
            )
        ]

    def added(self) -> list[bool]:
        return self._added

    def grade(self, grade: int) -> list[str]:
        return sorted([name for name, g in self._dict_students.items() if g == grade])
