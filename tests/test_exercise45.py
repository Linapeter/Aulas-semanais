
from exercises.exercise45_PE22 import names_scores

with open("tests/data/exercise45.txt", "r") as file:
    content = file.read()

names = content.replace('"', '').split(',')

def test_exercise45() -> None:
    assert names_scores(names) == 871_198_282
