from typing import Optional

import pytest


def threeSum(nums: list[int]) -> list[list[int]]:
    """
    [-1, 0, 1, 2, -1, -4]


    """

    triplets = set()
    
    # print(nums)
    for target_idx, target in enumerate(nums):
        nums_seen = set()
        for idx, num in enumerate(nums):
            # skip target_idx
            if idx == target_idx:
                continue

            # if we've seen (-target - num), then there
            # exists target + num + (-target - num) = 0
            if (-target - num) in nums_seen:
                triplet = sorted([target, num, -target - num])
                triplets.add(tuple(triplet))

            # print(triplets)

            nums_seen.add(num)

    return list(triplets)


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
