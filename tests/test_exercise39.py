from python.exercise39_PE19 import calendar, first_of_month
from datetime import date

def test_exercise39() -> None:
    assert 171 == calendar(2000).first_weekdays_gap_years("Sunday", 1901, 2000)
    assert 171 == first_of_month("Sunday", date(1901,1,1), date(2000,12,31))