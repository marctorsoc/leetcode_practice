from collections import defaultdict

import pytest


def twoSum(nums: list[int], target: int) -> list[int]:
    # Best solution: O(n) time + O(n) space
    # num_to_index = dict()
    # for idx, num in enumerate(nums):
    #     if target - num in num_to_index:
    #         return [num_to_index[target - num], idx]
    #     num_to_index[num] = idx

    # Another solution with O(n * logn) time and O(n) space
    # but if it was sorted would be O(1) space
    nums_with_indexes = sorted(  # [(idx, num), ...]
        enumerate(nums),
        key=lambda t: t[1],
    )
    left, right = 0, len(nums) - 1
    while left < right:
        print(left, right)
        left_idx, left_num = nums_with_indexes[left]
        right_idx, right_num = nums_with_indexes[right]

        s = left_num + right_num
        if s == target:
            return (
                [left_idx, right_idx] if left_idx < right_idx else [right_idx, left_idx]
            )
        elif s < target:
            # skip dups
            while nums_with_indexes[left][1] == left_num and left < right:
                left += 1
        else:  # s > 0
            # skip dups
            while nums_with_indexes[right][1] == right_num and left < right:
                right -= 1


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        # ([2, 7, 11, 15], 9, [0, 1]),
        # ([3, 2, 4], 6, [1, 2]),
        # ([3, 3], 6, [0, 1]),
        ([-1, 0, 1, 2, -1, -4], -3, [2, 5]),
    ],
)
def test_twoSum(nums, target, expected):
    assert twoSum(nums, target) == expected
