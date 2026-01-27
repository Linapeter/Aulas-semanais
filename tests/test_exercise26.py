from typing import List

import pytest

from python.exercise26_SliceSeries import slice_series


@pytest.mark.parametrize(
    "series, length, expected",
    [
        ("1", 1, ["1"]),
        ("12", 1, ["1", "2"]),
        ("35", 2, ["35"]),
        ("9142", 2, ["91", "14", "42"]),
        ("777777", 3, ["777", "777", "777", "777"]),
        (
            "918493904243",
            5,
            [
                "91849",
                "18493",
                "84939",
                "49390",
                "93904",
                "39042",
                "90424",
                "04243",
            ],
        ),
    ],
    ids=[
        "single digit, slice length 1",
        "two digits, slice length 1",
        "two digits, slice length 2",
        "overlapping slices",
        "duplicate slices",
        "long series",
    ],
)
def test_valid_slices(
    series: str,
    length: int,
    expected: List[str],
) -> None:
    result: List[str] = slice_series(series, length)
    assert result == expected, (
        f"slice_series(series={series!r}, length={length}) returned {result!r}, "
        f"expected {expected!r}"
    )


@pytest.mark.parametrize(
    "series, length, error_message",
    [
        ("12345", 6, "slice length cannot be greater than series length"),
        ("12345", 42, "slice length cannot be greater than series length"),
        ("12345", 0, "slice length cannot be zero"),
        ("123", -1, "slice length cannot be negative"),
        ("", 1, "series cannot be empty"),
    ],
    ids=[
        "slice length too large",
        "slice length way too large",
        "slice length zero",
        "slice length negative",
        "empty series",
    ],
)
def test_invalid_slices(
    series: str,
    length: int,
    error_message: str,
) -> None:
    with pytest.raises(ValueError, match=error_message):
        slice_series(series, length)
