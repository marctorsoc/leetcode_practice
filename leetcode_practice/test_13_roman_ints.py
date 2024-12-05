from collections import defaultdict
from typing import Optional

import pytest

char_to_num = {
    "V": 5,
    "X": 10,
    "I": 1,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def exercise(s: str) -> int:
    """
    LVIII -> 58
    """
    # check char by char
    # if no last num, then add value to buffer
    # if last num, then two cases:
    #  a) same value, add to total
    #  a) lower value, add to total
    #  b) higher value, add higher value - 2 * last_num

    last_num = char_to_num[s[0]]
    total = last_num

    for c in s[1:]:
        num = char_to_num[c]
        # if lower or equal just sum and record last num
        if num <= last_num:
            total += num
            last_num = num
        # but if higher, then add number - 2 * last num
        else:
            total += num - 2 * last_num

    return total
            

@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            "LVIII",
            58,
        ),
        (
            "III",
            3,
        ),
        (
            "MCMXCIV",
            1994,
        ),
    ],
)
def test_exercise(input_data, expected):
    assert exercise(input_data) == expected
