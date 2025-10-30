from os.path import join
from pathlib import Path

from exercises.exercise23 import grid_largest_product

BOX = str(
    " ".join(
        line.rstrip()
        for line in Path(join(Path(__file__).parent, "data", "exercise23.txt")).open()
    )
)


def test_exercise23() -> None:
    assert 70_600_674 == grid_largest_product(BOX, 20, 4)
