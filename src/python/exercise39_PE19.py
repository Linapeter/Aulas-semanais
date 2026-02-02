# Poject Euler
# Problem 19

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date


class calendar:
    """A class for basic calendar computations based on the Gregorian calendar.

    This class provides utilities to:
    - determine whether a year is a leap year;
    - compute the first weekday of a given year;
    - determine the number of days in a month;
    - count how many months in a year start on a given weekday;
    - aggregate this count over a range of years.

    Weekdays are represented internally as integers from 0 to 6.
    """

    days_per_month: dict[str, int] = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    weekday: dict[str, int] = {
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6,
        "Saturday": 0,
        "Sunday": 1,
    }

    def __init__(self, year: int) -> None:
        """Initialize a calendar instance for a given year.

        Parameters
        ----------
        year : int
            The year associated with the calendar instance.
        """
        self.year = year

    def is_leap(self, year: int) -> bool:
        """Determine whether a given year is a leap year.

        A leap year follows the Gregorian calendar rules:
        - divisible by 4 and not divisible by 100, or
        - divisible by 400.

        Parameters
        ----------
        year : int
            The year to be checked.

        Returns
        -------
        bool
            True if the year is a leap year, False otherwise.
        """
        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            return True
        else:
            return False

    def __repr__(self) -> str:
        """Return a human-readable representation of the calendar instance.

        The representation indicates whether the instance year is a leap year.

        Returns
        -------
        str
            A string stating whether the year is a leap year.
        """
        return (
            f"The year {self.year} is a leap year"
            if self.is_leap(self.year)
            else f"The year {self.year} isn't a leap year"
        )

    # 1 Jan 1900 was a Monday.
    def first_day_of_year(self, year: int) -> int:
        """Compute the weekday of January 1st for a given year.

        This calculation is based on the reference that
        January 1st, 1900 was a Monday.

        Parameters
        ----------
        year : int
            The year for which the first weekday is computed.

        Returns
        -------
        int
            An integer between 0 and 6 representing the weekday.
        """
        leap_years = sum(1 for years in range(1900, year) if self.is_leap(years))
        return ((year - 1900) + leap_years + 2) % 7

    def days_in_month(self, month: str, year: int) -> int:
        """Return the number of days in a given month of a given year.

        February is adjusted to 29 days in leap years.

        Parameters
        ----------
        month : str
            The month name (e.g., "February").
        year : int
            The year of interest.

        Returns
        -------
        int
            The number of days in the specified month.
        """
        if month == "February" and self.is_leap(year):
            return 29
        return self.days_per_month[month]

    def first_weekday_of_months(self, weekday: str, year: int) -> int:
        """Count how many months in a given year start on a specific weekday.

        Parameters
        ----------
        weekday : str
            The weekday name (e.g., "Monday").
        year : int
            The year to be evaluated.

        Returns
        -------
        int
            The number of months whose first day falls on the given weekday.
        """
        weekday_int = self.weekday[weekday]
        first_day = self.first_day_of_year(year)

        count = 0
        sum_days = 0

        for month in self.days_per_month:
            if (first_day + sum_days) % 7 == weekday_int:
                count += 1
            sum_days += self.days_in_month(month, year)

        return count

    def first_weekdays_gap_years(self, weekday: str, start: int, final: int) -> int:
        """Count how many months start on a given weekday over a range of years.

        The range is inclusive of both the start and final years.

        Parameters
        ----------
        weekday : str
            The weekday name (e.g., "Sunday").
        start : int
            The starting year.
        final : int
            The ending year.

        Returns
        -------
        int
            The total number of months starting on the given weekday
            across the specified year range.
        """
        total = 0
        for year in range(start, final + 1):
            total += self.first_weekday_of_months(weekday, year)
        return total


def first_of_month(weekday: str, start: date, final: date) -> int:
    """
    Count how many times the first day of a month falls on a given weekday
    within a date range.
    """
    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    weekday_int = weekdays[weekday]
    count = 0

    year, month = start.year, start.month

    while date(year, month, 1) <= final:

        count += date(year, month, 1).weekday() == weekday_int  # if TRUE += 1 else += 0
        month, year = (1, year + 1) if month == 12 else (month + 1, year)

    return count
