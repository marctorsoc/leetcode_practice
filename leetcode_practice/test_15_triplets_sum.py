from typing import Optional

import pytest


def threeSum(nums: list[int]) -> list[list[int]]:
    """
    [-1, 0, 1, 2, -1, -4]
    sort [-4 -1, -1, 0, 1, 2]


    """
    nums.sort()

    triplets = []
    for target_idx, target in enumerate(nums):

        # skip duplicates for the target
        if target_idx > 0 and target == nums[target_idx - 1]:
            continue

        left, right = target_idx + 1, len(nums) - 1
        while left < right:

            print(target, left, right, triplets)

            left_num, right_num = nums[left], nums[right]
            s = target + left_num + right_num

            if s == 0:
                triplets.append([target, left_num, right_num])

                left = move_left(nums, left, right)
                right = move_right(nums, left, right)

            elif s < 0:
                left = move_left(nums, left, right)
            else:
                right = move_right(nums, left, right)
    return triplets

def move_left(nums, left, right):
    while left < right and nums[left + 1] == nums[left]:
        left += 1
    return left + 1

def move_right(nums, left, right):
    while left < right and nums[right - 1] == nums[right]:
        right -= 1
    return right - 1


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        (
            [-1, 0, 1, 2, -1, -4],
            [[-1, -1, 2], [-1, 0, 1]],
        ),
    ],
)
def test_exercise(nums, expected):
    assert threeSum(nums) == expected
