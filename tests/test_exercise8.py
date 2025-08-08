
from exercises.exercise8 import SpaceAge

def test_age_on_earth() -> None:
    assert SpaceAge(1_000_000_000).on_earth() == 31.69

def test_age_on_mercury() -> None:
    assert SpaceAge(2134835688).on_mercury() == 280.88

def test_age_on_venus() -> None:
    assert SpaceAge(189839836).on_venus() == 9.78

def test_age_on_mars() -> None:
    assert SpaceAge(2129871239).on_mars() == 35.88

def test_age_on_jupiter() -> None:
    assert SpaceAge(901876382).on_jupiter() == 2.41

def test_age_on_saturn() -> None:
    assert SpaceAge(2000000000).on_saturn() == 2.15

def test_age_on_uranus() -> None:
    assert SpaceAge(1210123456).on_uranus() == 0.46

def test_age_on_neptune() -> None:
    assert SpaceAge(1821023456).on_neptune() == 0.35
