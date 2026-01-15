from exercises.exercise39_PE19 import calendar


def test_exercise39() -> None:
    assert 171 == calendar(2000).first_weekdays_gap_years("Sunday", 1901, 2000)
