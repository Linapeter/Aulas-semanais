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

    leap_years: list[int] = []

    def __init__(self, year: int) -> None:
        self.year = year

        for i in range(1900, year):
            if (i % 4 == 0 and i % 100 != 0) or (i % 100 == 0 and i % 400 == 0):
                self.leap_years.append(i)

        if year in self.leap_years:
            self.days_per_month["February"] = 29

    def __repr__(self) -> str:
        return (
            f"The year {self.year} is a leap year"
            if self.year in self.leap_years
            else f"The year {self.year} isn't a leap year"
        )

    # 1 Jan 1900 was a Monday.
    def first_day_of_year(self, year: int) -> int:
        weekday = ((year - 1900) + len(self.leap_years) + 2) % 7
        return weekday

    def first_weekday_of_months(self, weekday: str, year: int) -> int:
        weekday_int = self.weekday[weekday]

        count = 0
        sum_days = 0
        if self.first_day_of_year(year) == weekday_int:
            count = 1

        for _, days in self.days_per_month.items():
            if (self.first_day_of_year(year) + sum_days) % 7 == weekday_int:
                count += 1
            sum_days += days

        return count

    def first_weekdays_gap_years(self, weekday: str, start: int, final: int) -> int:
        total = 0
        for year in range(start, final + 1):
            total += self.first_weekday_of_months(weekday, year)
        return total


c = calendar(2000)
print(c)
print(c.first_day_of_year(2000))
print(c.first_weekday_of_months("Sunday", 2000))
print(c.first_weekdays_gap_years("Sunday", 1901, 2000))
