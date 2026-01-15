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


class calendar:

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
        self.year = year

    def is_leap(self, year: int) -> bool:
        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return (
            f"The year {self.year} is a leap year"
            if self.is_leap(self.year)
            else f"The year {self.year} isn't a leap year"
        )

    # 1 Jan 1900 was a Monday.
    def first_day_of_year(self, year: int) -> int:
        leap_years = sum(1 for years in range(1900, year) if self.is_leap(years))
        return ((year - 1900) + leap_years + 2) % 7

    def days_in_month(self, month: str, year: int) -> int:
        if month == "February" and self.is_leap(year):
            return 29
        return self.days_per_month[month]

    def first_weekday_of_months(self, weekday: str, year: int) -> int:
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
        total = 0
        for year in range(start, final + 1):
            total += self.first_weekday_of_months(weekday, year)
        return total
