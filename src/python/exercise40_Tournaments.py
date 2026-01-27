# Tournament

# Instructions
# Tally the results of a small football competition.

# Based on an input file containing which team played against which and what the outcome was, create a file with a table like this:

# Team                           | MP |  W |  D |  L |  P
# Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
# Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
# Blithering Badgers             |  3 |  1 |  0 |  2 |  3
# Courageous Californians        |  3 |  0 |  1 |  2 |  1
# What do those abbreviations mean?

# MP: Matches Played
# W: Matches Won
# D: Matches Drawn (Tied)
# L: Matches Lost
# P: Points
# A win earns a team 3 points. A draw earns 1. A loss earns 0.

# The outcome is ordered by points, descending. In case of a tie, teams are ordered alphabetically.

# Input
# Your tallying program will receive input that looks like:

# Allegoric Alaskans;Blithering Badgers;win
# Devastating Donkeys;Courageous Californians;draw
# Devastating Donkeys;Allegoric Alaskans;win
# Courageous Californians;Blithering Badgers;loss
# Blithering Badgers;Devastating Donkeys;loss
# Allegoric Alaskans;Courageous Californians;win
# The result of the match refers to the first team listed. So this line:

# Allegoric Alaskans;Blithering Badgers;win
# means that the Allegoric Alaskans beat the Blithering Badgers.

# This line:

# Courageous Californians;Blithering Badgers;loss
# means that the Blithering Badgers beat the Courageous Californians.

# And this line:
# "Allegoric Alaskans;Blithering Badgers;win",
# "Blithering Badgers;Courageous Californians;win",
# "Courageous Californians;Allegoric Alaskans;loss",
# ],
# [
# HEADER,
# "Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6",
# "Blithering Badgers             |  2 |  1 |  0 |  1 |  3",
# "Courageous Californians        |  2 |  0 |  0 |  2 |  0",
# ],

# Team                           | MP |  W |  D |  L |  P


# Devastating Donkeys;Courageous Californians;draw
# means that the Devastating Donkeys and Courageous Californians tied.

from numpy import array, ndarray

def tally(rows: list[str]) -> list[str]:
    """Generate a formatted standings table from match results.

    Each match result is provided as a string in the format:
        "team1;team2;result"

    where `result` refers to the outcome from the perspective of `team1` and
    can be one of:
        - "win"
        - "draw"
        - "loss"

    For each team, the following statistics are computed:
        - MP: Matches Played
        - W : Wins
        - D : Draws
        - L : Losses
        - P : Points

    Points are assigned according to standard rules:
        - win  -> 3 points
        - draw -> 1 point
        - loss -> 0 points

    The final table is sorted by:
        1. Total points (descending)
        2. Number of wins (descending)
        3. Team name (alphabetical order)

    Parameters
    ----------
    rows : list[str]
        A list of match result strings formatted as
        "team1;team2;result".

    Returns
    -------
    list[str]
        A list of formatted strings representing the standings table,
        including a header row.
    """
    teams: dict[str, ndarray] = {}

    for row in rows:
        team1, team2, result = row.split(";")
        if team1 not in teams:
            teams[team1] = array([0, 0, 0, 0, 0])
        if team2 not in teams:
            teams[team2] = array([0, 0, 0, 0, 0])

        if result == "win":
            teams[team1] += array([1, 1, 0, 0, 3])
            teams[team2] += array([1, 0, 0, 1, 0])
        if result == "draw":
            teams[team1] += array([1, 0, 1, 0, 1])
            teams[team2] += array([1, 0, 1, 0, 1])
        if result == "loss":
            teams[team1] += array([1, 0, 0, 1, 0])
            teams[team2] += array([1, 1, 0, 0, 3])

    table = [("Team", "MP", "W", "D", "L", "P")]
    ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
    sorted_teams = sorted(teams.items(), key=lambda t: (-t[1][4], -t[1][1], t[0]))

    for name, numbers in sorted_teams:
        table.append((name, *numbers))

    return [ROW_FORMAT.format(*row) for row in table]
