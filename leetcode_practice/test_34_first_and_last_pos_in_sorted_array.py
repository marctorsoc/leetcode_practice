from typing import List, Optional

import pytest


def exercise(nums: List[int], target: int) -> List[int]:
    """
    1  2  3  4  6  6  6  7  7  8  8  8  9  9  9  9                            

    right target = 6
    1  2  3  4  6  6  6  7
             4  6  6  6  7
                   6  6  7
                      6  7
                      6

    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    
    while left < right:
        get center middle point
        if center = target and left: keep the left part
        if center = target and right: keep the right part
        if center > target: keep the left part
        if center < target: keep the right part

    """

    def modified_binary_search(array, target, is_left):
        left, right = 0, len(array) - 1
        idx = -1
        while left <= right:
            center = (left + right) // 2
            if array[center] < target:  # keep right part
                left = center + 1
            elif array[center] > target:  # keep left part
                right = center - 1
            elif is_left:  # keep the left part
                idx = center
                right = center - 1
            else:  # keep the right part
                idx = center
                left = center + 1
        
        return idx
    
    left = modified_binary_search(nums, target, is_left=True)
    right = modified_binary_search(nums, target, is_left=False)

    return [left, right]
    

@pytest.mark.parametrize(
    ("input_data", "target", "expected"),
    [
        ([5,7,7,8,8,10], 8, [3,4]),
        ([5,7,7,8,8,10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([2,2], 2, [0, 1]),
    ],
)
def test_exercise(input_data, target, expected):
    assert exercise(input_data, target) == expected
