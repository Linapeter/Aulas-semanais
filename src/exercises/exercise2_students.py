# Exercise 2

# Students Class created to receive name and grade


class students:
    """Manage a collection of students and their grades.

    Students are stored internally as a mapping from name to grade.
    The class also keeps track of whether each call to `add_student`
    successfully added a new student.
    """

    def __init__(self) -> None:
        """Initialize an empty student registry.

        Attributes
        ----------
        _dict_students : dict[str, int]
            Dictionary mapping student names to their grades.
        _added : list[bool]
            List indicating whether each call to `add_student` resulted
            in a successful insertion.
        """
        self._dict_students: dict[str, int] = {}
        self._added: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student with a given grade.

        If the student name does not already exist, the student is added
        and `True` is appended to the added list. Otherwise, the student
        is not added and `False` is appended.

        Parameters
        ----------
        name : str
            The student's name.
        grade : int
            The student's grade.
        """
        if name not in self._dict_students:
            self._dict_students[name] = grade
            self._added.append(True)
        else:
            self._added.append(False)

    def roster(self) -> list[str]:
        """Return the list of student names ordered by grade and name.

        Students are sorted first by grade (ascending) and then
        alphabetically by name.

        Returns
        -------
        list[str]
            Sorted list of student names.
        """
        return [
            name
            for name, _ in sorted(
                self._dict_students.items(), key=lambda x: (x[1], x[0])
            )
        ]

    def added(self) -> list[bool]:
        """Return the history of add_student operations.

        Each element indicates whether the corresponding call to
        `add_student` successfully added a new student.

        Returns
        -------
        list[bool]
            List of boolean values indicating successful insertions.
        """
        return self._added

    def grade(self, grade: int) -> list[str]:
        """Return the names of students with a given grade.

        The returned list is sorted alphabetically.

        Parameters
        ----------
        grade : int
            Grade to filter students by.

        Returns
        -------
        list[str]
            Alphabetically sorted list of student names with the given grade.
        """
        return sorted([name for name, g in self._dict_students.items() if g == grade])
