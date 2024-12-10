from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(nums: list[int], target: int) -> int:
    """
    sorted unique ints

    1  3  5  6  8  10  12
    0  1  2  3  4   5   6
                l   r    
    

    2

    """
    left, right = 0, len(nums) - 1
    if nums[left] >= target:
        return left
    if nums[right] == target:
        return right
    if nums[right] < target:
        return right + 1
    
    while left < right - 1:
        center = (left + right) // 2
        center_num = nums[center]
        if center_num == target:
            return center
        if center_num < target:
            left = center
        else:
            right = center

    return right


@pytest.mark.parametrize(
    ("input_data", "target", "expected"),
    [
        (
            [1,3,5,6], 5, 2
        ),
        (
            [1,3,5,6], 2, 1
        ),
        (
            [1,3,5,6], 7, 4
        )
    ],
)
def test_exercise(input_data, target, expected):
    assert exercise(input_data, target) == expected
