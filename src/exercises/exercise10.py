# Your task is to determine the date and time one gigasecond after a certain date.
# A gigasecond is one thousand million seconds. That is a one with nine zeros after it.
# If you were born on January 24th, 2015 at 22:00 (10:00:00pm),
# then you would be a gigasecond old on October 2nd, 2046 at 23:46:40 (11:46:40pm).

from datetime import datetime, timedelta

class one_giga_date:
    one_giga_seconds = timedelta(seconds=1e9)
    def __init__(self, date:datetime) -> None:
        self.date = date
    def __repr__(self) -> str:
        return self.date.strftime("Ano de %Y, do mês %m, do dia %d (%H:%M:%S)")
    def add(self) -> datetime:
        return self.date + self.one_giga_seconds