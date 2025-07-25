# Exercise 2

# Students Class created to receive name and grade
class students:
    list_students = []
    def __init__(self,name,grade: str,int) -> None:
        self.name = name
        self.grade = int(grade)
        students.list_students.append((self.grade, self.name))

    def get_name(self) -> str:
        return self.name
    def get_grade(self) -> int:
        return self.grade

    def set_grade(self, grade: int) -> None:
        self.grade = grade

    def __repr__(self) -> str:
        return f"Student {self.name} in grade {self.grade}."

    # Sorting students by grade and name
    def sort_students(self)-> list[Any]:
        sorted_list = sorted(students.list_students, key=lambda x: (x[0], x[1]))
        return [x[1] for x in sorted_list]

# Function to return students by grade
def by_grade(grade) -> list[Any]:
    in_grade = sorted(students.list_students, key=lambda x: x[0])
    return [x[1] for x in in_grade if x[0] == grade]