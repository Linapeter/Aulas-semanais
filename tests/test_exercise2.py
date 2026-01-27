from typing import Any

from python.exercise2_students import students


def test_roster_is_empty_when_no_student_is_added() -> None:
    s = students()
    expected: list[Any] = []
    assert s.roster() == expected


def test_add_a_student() -> None:
    s = students()
    s.add_student(name="Aimee", grade=2)
    expected = [True]
    assert s.added() == expected


def test_student_is_added_to_the_roster() -> None:
    s = students()
    s.add_student(name="Aimee", grade=2)
    expected = ["Aimee"]
    assert s.roster() == expected


def test_adding_multiple_students_in_the_same_grade_in_the_roster() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="Paul", grade=2)
    expected = [True, True, True]
    assert s.added() == expected


def test_multiple_students_in_the_same_grade_are_added_to_the_roster() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="Paul", grade=2)
    expected = ["Blair", "James", "Paul"]
    assert s.roster() == expected


def test_cannot_add_student_to_same_grade_in_the_roster_more_than_once() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="Paul", grade=2)
    expected = [True, True, False, True]
    assert s.added() == expected


def test_student_not_added_to_same_grade_in_the_roster_more_than_once() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="Paul", grade=2)
    expected = ["Blair", "James", "Paul"]
    assert s.roster() == expected


def test_adding_students_in_multiple_grades() -> None:
    s = students()
    s.add_student(name="Chelsea", grade=3)
    s.add_student(name="Logan", grade=7)
    expected = [True, True]
    assert s.added() == expected


def test_students_in_multiple_grades_are_added_to_the_roster() -> None:
    s = students()
    s.add_student(name="Chelsea", grade=3)
    s.add_student(name="Logan", grade=7)
    expected = ["Chelsea", "Logan"]
    assert s.roster() == expected


def test_cannot_add_same_student_to_multiple_grades_in_the_roster() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="James", grade=3)
    s.add_student(name="Paul", grade=3)
    expected = [True, True, False, True]
    assert s.added() == expected


def test_student_not_added_to_multiple_grades_in_the_roster() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="James", grade=3)
    s.add_student(name="Paul", grade=3)
    expected = ["Blair", "James", "Paul"]
    assert s.roster() == expected


def test_students_are_sorted_by_grades_in_the_roster() -> None:
    s = students()
    s.add_student(name="Jim", grade=3)
    s.add_student(name="Peter", grade=2)
    s.add_student(name="Anna", grade=1)
    expected = ["Anna", "Peter", "Jim"]
    assert s.roster() == expected


def test_students_are_sorted_by_name_in_the_roster() -> None:
    s = students()
    s.add_student(name="Peter", grade=2)
    s.add_student(name="Zoe", grade=2)
    s.add_student(name="Alex", grade=2)
    expected = ["Alex", "Peter", "Zoe"]
    assert s.roster() == expected


def test_students_are_sorted_by_grades_and_then_by_name_in_the_roster() -> None:
    s = students()
    s.add_student(name="Peter", grade=2)
    s.add_student(name="Anna", grade=1)
    s.add_student(name="Barb", grade=1)
    s.add_student(name="Zoe", grade=2)
    s.add_student(name="Alex", grade=2)
    s.add_student(name="Jim", grade=3)
    s.add_student(name="Charlie", grade=1)
    expected = ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"]
    assert s.roster() == expected


def test_grade_is_empty_if_no_students_in_the_roster() -> None:
    s = students()
    expected: list[Any] = []
    assert s.grade(1) == expected


def test_grade_is_empty_if_no_students_in_that_grade() -> None:
    s = students()
    s.add_student(name="Peter", grade=2)
    s.add_student(name="Zoe", grade=2)
    s.add_student(name="Alex", grade=2)
    s.add_student(name="Jim", grade=3)
    expected: list[Any] = []
    assert s.grade(1) == expected


def test_student_not_added_to_same_grade_more_than_once() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="Paul", grade=2)
    expected = ["Blair", "James", "Paul"]
    assert s.grade(2) == expected


def test_student_not_added_to_multiple_grades() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="James", grade=3)
    s.add_student(name="Paul", grade=3)
    expected = ["Blair", "James"]
    assert s.grade(2) == expected


def test_student_not_added_to_other_grade_for_multiple_grades() -> None:
    s = students()
    s.add_student(name="Blair", grade=2)
    s.add_student(name="James", grade=2)
    s.add_student(name="James", grade=3)
    s.add_student(name="Paul", grade=3)
    expected = ["Paul"]
    assert s.grade(3) == expected


def test_students_are_sorted_by_name_in_a_grade() -> None:
    s = students()
    s.add_student(name="Franklin", grade=5)
    s.add_student(name="Bradley", grade=5)
    s.add_student(name="Jeff", grade=1)
    expected = ["Bradley", "Franklin"]
    assert s.grade(5) == expected
