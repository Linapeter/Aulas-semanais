from os.path import join
from pathlib import Path

from exercises.exercise27_PE13 import large_sum

BOX = str(
    " ".join(
        line.rstrip()
        for line in Path(join(Path(__file__).parent, "data", "exercise27.txt")).open()
    )
)


def test_exercise27() -> None:
    assert 5_537_376_230 == large_sum(BOX)
