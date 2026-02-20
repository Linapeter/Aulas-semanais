from os.path import join
from pathlib import Path

from exercises.exercise37_PE18 import maximum_path_sum

triangle = str(
    "\n".join(
        line.rstrip()
        for line in Path(join(Path(__file__).parent, "data", "exercise37.txt")).open()
    )
)

def test_exercise37() -> None:
    assert maximum_path_sum(triangle) == 1_074
