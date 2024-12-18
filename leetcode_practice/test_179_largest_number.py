import functools
from typing import List, Optional

import pytest


def exercise(nums: List[int]) -> str:
    """ """



















    #######################################################

    def customSort(a: str, b: str) -> int:
        if a + b == b + a:
            return 0
        return -1 if a + b < b + a else 1

    sorted_nums = sorted(
        map(str, nums), key=functools.cmp_to_key(customSort), reverse=True
    )
    if sorted_nums[0] == '0':
        return '0'
    return "".join(sorted_nums)


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            [10, 2],
            "210",
        ),
        (
            [3, 30, 34, 5, 9],
            "9534330",
        ),
        (
            [34323, 3432],
            "343234323",
        ),
    ],
    ids=[1, 2, 3],
)
def test_exercise(input_data, expected):
    assert exercise(input_data) == expected
