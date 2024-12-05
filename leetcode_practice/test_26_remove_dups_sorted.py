from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(nums: List[int]) -> int:
    k = 1
    for idx in range(1, len(nums)):
        if nums[idx] != nums[k - 1]:
            nums[k] = nums[idx]
            k += 1
    return k

@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            [1,1,2],
            [1,2],
        ),
        (
            [0,0,1,1,1,2,2,3,3,4],
            [0,1,2,3,4],
        ),
        # (
            
        # ),
        # (
        #     [-2, -5, -3],
        #     -2,
        # )
    ],
)
def test_exercise(input_data, expected):
    exercise(input_data)
    for idx in range(len(expected)):
        assert input_data[idx] == expected[idx]
