from typing import List, Optional

import pytest


def exercise(nums: List[int], target: int) -> List[int]:
    """
    [5,7,7,8,8,8,8,10] --> [3, 6]

    nums = [5,7,7,7,7,7,8,8,8,8, 8, 8, 8, 8, 9]
    idx  =  0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
            l             c                  r  
            l     c     r
            l   c     r   
            l   c     r   

    """
    if not nums:
        return [-1, -1]

    left, right = 0, len(nums) - 1
    while left <= right:
        center = (left + right) // 2
        # print(left, right, center)
        # import pdb; pdb.set_trace()
        if nums[center] == target:
            break
        elif nums[center] < target:
            left = center + 1
        else:
            right = center - 1

    # at this point we know that nums[center] = target
    # but check if that's not the case
    if nums[center] != target:
        return [-1, -1]

    left = right = center
    while left > 0 and nums[left - 1] == target:
        left -= 1
    while right < len(nums) - 1 and nums[right + 1] == target:
        right += 1

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
