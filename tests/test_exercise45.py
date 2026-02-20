from exercises.exercise45_PE22 import names_scores
from os.path import join
from pathlib import Path

with open(Path(join(Path(__file__).parent, "data", "exercise45.txt"))) as file:
    content = file.read()
    names = content.replace('"', '').split(',')

def test_exercise45() -> None:
    assert names_scores(names) == 871_198_282
