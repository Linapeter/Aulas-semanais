from datetime import datetime

from exercises.exercise10_onegigadate import one_giga_date

def test_date_only_specification_of_time() -> None:
    assert one_giga_date(datetime(2011, 4, 25, 0, 0)).add() == datetime(2043, 1, 1, 1, 46, 40)


def test_second_test_for_date_only_specification_of_time() -> None:
    assert one_giga_date(datetime(1977, 6, 13, 0, 0)).add() == datetime(2009, 2, 19, 1, 46, 40)


def test_third_test_for_date_only_specification_of_time() -> None:
    assert one_giga_date(datetime(1959, 7, 19, 0, 0)).add() == datetime(1991, 3, 27, 1, 46, 40)


def test_full_time_specified() -> None:
    assert one_giga_date(datetime(2015, 1, 24, 22, 0)).add() == datetime(2046, 10, 2, 23, 46, 40)


def test_full_time_with_day_roll_over() -> None:
    assert one_giga_date(datetime(2015, 1, 24, 23, 59, 59)).add() == datetime(2046, 10, 3, 1, 46, 39)
