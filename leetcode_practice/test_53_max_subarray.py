from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(nums: List[int]) -> int:
    current_max, global_max = nums[0], nums[0]
    for num in nums[1:]:
        current_max = max(num, num + current_max)
        global_max = max(current_max, global_max)

    return global_max


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            6,
        ),
        (
            [1],
            1,
        ),
        (
            [5, 4, -1, 7, 8],
            23,
        ),
        (
            [-2, -5, -3],
            -2,
        )
    ],
)
def test_exercise(input_data, expected):
    assert exercise(input_data) == expected
