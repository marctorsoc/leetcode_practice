from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(height: List[int]) -> int:
    """
    1  3  4  2  5  4  8  3  7
    """















    ########################################



    left, right = 0, len(height) - 1
    maxArea = 0

    while left < right:
        numLeft, numRight = height[left], height[right]
        area = min(numLeft, numRight) * (right - left)
        maxArea = max(maxArea, area)
        if numLeft < numRight:
            left += 1
        else:
            right -= 1

    return maxArea    


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            [1,8,6,2,5,4,8,3,7],
            49,
        ),
        (
            [1,1],
            1,
        )
    ],
)
def test_exercise(input_data, expected):
    assert exercise(input_data) == expected
