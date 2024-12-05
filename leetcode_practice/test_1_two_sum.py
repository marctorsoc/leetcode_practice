from collections import defaultdict

import pytest


def twoSum(nums: list[int], target: int) -> list[int]:
    # Best solution: O(N) space and O(N) time
    # num_to_idx = dict()
    # for idx, num in enumerate(nums):
    #     comp = target - num
    #     if comp in num_to_idx:
    #         return [num_to_idx[comp], idx]
    #     num_to_idx[num] = idx


    # Another solution with 2-pointer and NOT coming sorted -- n * logn
    nums_with_orig_indices = list(enumerate(nums))
    nums_with_orig_indices.sort(key=lambda t: t[1])  # O( n * logn )

    left, right = 0, len(nums) - 1
    while left < right:  # O(n)
        left_idx, left_num = nums_with_orig_indices[left]
        right_idx, right_num = nums_with_orig_indices[right]

        s = left_num + right_num

        if s == target:
            return sorted([left_idx, right_idx])
        if s < target:
            left += 1
        else:
            right -= 1


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, 0, 1, 2, -1, -4], -3, [2, 5]),
    ],
)
def test_twoSum(nums, target, expected):
    assert twoSum(nums, target) == expected
