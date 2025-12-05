# One Earth year equals 365.25 Earth days, or 31,557,600 seconds.
# If you were told someone was 1,000,000,000 seconds old, their age would be 31.69 Earth-years.

class SpaceAge:
    seconds_in_a_year_on_earth = 31_557_600
    PLANETS: dict[str, float] = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int) -> None:
        self.seconds = seconds
        self.__init_planets__()

    def __repr__(self) -> str:
        return f"Your age is {self.seconds} seconds."

    def __init_planets__(self) -> None:
        for planet, orbital_period in self.PLANETS.items():
            setattr(
                self,
                f"on_{planet}",
                lambda orbital_period=orbital_period: round(
                    self.seconds / self.seconds_in_a_year_on_earth / orbital_period, 2
                ),
            )
