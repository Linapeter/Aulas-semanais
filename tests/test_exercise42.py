from datetime import date

import pytest
from exercises.exercise42_meetup import MeetUp, MeetupDayException, MeetupError


@pytest.mark.parametrize(
    "year, month, weekday, expected",
    [
        (2013, 5, "Monday", date(2013, 5, 13)),
        (2013, 8, "Monday", date(2013, 8, 19)),
        (2013, 9, "Monday", date(2013, 9, 16)),
        (2013, 3, "Tuesday", date(2013, 3, 19)),
        (2013, 4, "Tuesday", date(2013, 4, 16)),
        (2013, 8, "Tuesday", date(2013, 8, 13)),
        (2013, 1, "Wednesday", date(2013, 1, 16)),
        (2013, 2, "Wednesday", date(2013, 2, 13)),
        (2013, 6, "Wednesday", date(2013, 6, 19)),
        (2013, 5, "Thursday", date(2013, 5, 16)),
        (2013, 6, "Thursday", date(2013, 6, 13)),
        (2013, 9, "Thursday", date(2013, 9, 19)),
        (2013, 4, "Friday", date(2013, 4, 19)),
        (2013, 8, "Friday", date(2013, 8, 16)),
        (2013, 9, "Friday", date(2013, 9, 13)),
        (2013, 2, "Saturday", date(2013, 2, 16)),
        (2013, 4, "Saturday", date(2013, 4, 13)),
        (2013, 10, "Saturday", date(2013, 10, 19)),
        (2013, 5, "Sunday", date(2013, 5, 19)),
        (2013, 6, "Sunday", date(2013, 6, 16)),
        (2013, 10, "Sunday", date(2013, 10, 13)),
        (2022, 5, "Friday", date(2022, 5, 13)),
    ],
)
def test_teenth(year: int, month: int, weekday: str, expected: date) -> None:
    assert MeetUp(year, month, "teenth", weekday).meetup() == expected

@pytest.mark.parametrize(
    "year, month, week, weekday, expected",
    [
        (2013, 3, "first", "Monday", date(2013, 3, 4)),
        (2013, 4, "first", "Monday", date(2013, 4, 1)),
        (2013, 5, "first", "Tuesday", date(2013, 5, 7)),
        (2013, 6, "first", "Tuesday", date(2013, 6, 4)),
        (2013, 7, "first", "Wednesday", date(2013, 7, 3)),
        (2013, 8, "first", "Wednesday", date(2013, 8, 7)),
        (2013, 9, "first", "Thursday", date(2013, 9, 5)),
        (2013, 10, "first", "Thursday", date(2013, 10, 3)),
        (2013, 11, "first", "Friday", date(2013, 11, 1)),
        (2013, 12, "first", "Friday", date(2013, 12, 6)),
        (2013, 1, "first", "Saturday", date(2013, 1, 5)),
        (2013, 2, "first", "Saturday", date(2013, 2, 2)),
        (2013, 3, "first", "Sunday", date(2013, 3, 3)),
        (2013, 4, "first", "Sunday", date(2013, 4, 7)),

        (2013, 3, "second", "Monday", date(2013, 3, 11)),
        (2013, 4, "second", "Monday", date(2013, 4, 8)),
        (2013, 5, "second", "Tuesday", date(2013, 5, 14)),
        (2013, 6, "second", "Tuesday", date(2013, 6, 11)),

        (2013, 3, "third", "Monday", date(2013, 3, 18)),
        (2013, 4, "third", "Monday", date(2013, 4, 15)),

        (2013, 3, "fourth", "Monday", date(2013, 3, 25)),
        (2013, 4, "fourth", "Monday", date(2013, 4, 22)),

        (2013, 3, "last", "Monday", date(2013, 3, 25)),
        (2013, 4, "last", "Monday", date(2013, 4, 29)),
        (2012, 2, "last", "Wednesday", date(2012, 2, 29)),
        (2014, 12, "last", "Wednesday", date(2014, 12, 31)),
        (2015, 2, "last", "Sunday", date(2015, 2, 22)),
        (2024, 6, "last", "Sunday", date(2024, 6, 30)),
    ],
)
def test_weeks(year: int, month: int, week: str, weekday: str, expected: date) -> None:
    assert MeetUp(year, month, week, weekday).meetup() == expected

@pytest.mark.parametrize(
    "year, month, week, weekday",
    [
        (2022, 2, "fifth", "Monday"),
        (2022, 8, "fifth", "Friday"),
        (2023, 5, "fifth", "Thursday"),
    ],
)
def test_nonexistent_meetup_raises(year: int, month: int, week: str, weekday: str) -> None:
    with pytest.raises(MeetupDayException, match="That day does not exist."):
        MeetUp(year, month, week, weekday).meetup()
