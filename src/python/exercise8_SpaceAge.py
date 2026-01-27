# One Earth year equals 365.25 Earth days, or 31,557,600 seconds.
# If you were told someone was 1,000,000,000 seconds old, their age would be 31.69 Earth-years.


class SpaceAge:
    """Calculate age on different planets based on a given number of seconds.

    The age is computed by converting seconds into Earth years and then
    adjusting by each planet's orbital period relative to Earth.
    """

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

    def __init__(
        self,
        seconds: int,
    ) -> None:
        """Initialize the SpaceAge instance.

        Parameters
        ----------
        seconds : int
            Age expressed in seconds.
        """
        self.seconds = seconds
        self.__init_planets__()

    def __repr__(self) -> str:
        """Return a string representation of the object.

        Returns
        -------
        str
            A string showing the age in seconds.
        """
        return f"Your age is {self.seconds} seconds."

    def __init_planets__(self) -> None:
        """Dynamically create methods to compute age on each planet.

        For each planet in `PLANETS`, a method named `on_<planet>` is created.
        Each method returns the age in years on that planet, rounded to
        two decimal places.
        """
        for planet, orbital_period in self.PLANETS.items():
            setattr(
                self,
                f"on_{planet}",
                lambda orbital_period=orbital_period: round(
                    self.seconds / self.seconds_in_a_year_on_earth / orbital_period, 2
                ),
            )
