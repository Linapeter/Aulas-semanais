# One Earth year equals 365.25 Earth days, or 31,557,600 seconds.
# If you were told someone was 1,000,000,000 seconds old, their age would be 31.69 Earth-years.

seconds_in_a_year_on_earth = 31_557_600

class SpaceAge:
    def __init__(self, seconds:int) -> None:
        self.seconds = seconds
    def __repr__(self) -> str:
        return f"Your age is {self.seconds} seconds."

# Calc: seconds of living / seconds in one year
    def on_mercury(self) -> float:           # 0.2408467 = a year there
        a_year_on_mercury = 0.2408467
        self.age_on_mercury: float = self.seconds / (a_year_on_mercury*seconds_in_a_year_on_earth)
        return round(self.age_on_mercury,2)
    def on_venus(self) -> float:
        a_year_on_venus = 0.61519726
        self.age_on_venus: float = self.seconds / (a_year_on_venus*seconds_in_a_year_on_earth)
        return round(self.age_on_venus,2)

    def on_earth(self) -> float:
        return round(self.seconds / (seconds_in_a_year_on_earth),2)
    def on_mars(self) -> float:
        return round(self.seconds / (1.8808158*seconds_in_a_year_on_earth),2)
    def on_jupiter(self) -> float:
        return round(self.seconds / (11.862615*seconds_in_a_year_on_earth),2)
    def on_saturn(self) -> float:
        return round(self.seconds / (29.447498*seconds_in_a_year_on_earth),2)
    def on_uranus(self) -> float:
        return round(self.seconds / (84.016846*seconds_in_a_year_on_earth),2)
    def on_neptune(self) -> float:
        return round(self.seconds / (164.79132*seconds_in_a_year_on_earth),2)
