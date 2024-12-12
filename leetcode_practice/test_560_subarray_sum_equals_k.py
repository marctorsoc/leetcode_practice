from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(nums: List[int], k: int) -> int:
    """
    3  5  1  1  2  2  3  4
    0  1  2  3  4  5  6  7
    l  r

    brute-force

    O(n^2)

    for left in range(len(nums)):
        currentSum = nums[left]
        for right in range(1, len(nums)):
            currentSum += nums[right]
            if currentSum == k:
                append
                break



    advance left when sum is higher than k
    advance right when sum is lower than k
    restart sum and get left with right when sum = k

    """
    cumsum, combis = 0, 0
    cumsum_to_freq = defaultdict(int)
    cumsum_to_freq[0] = 1
    for num in nums:
        cumsum += num
        
        comp = cumsum - k
        if comp in cumsum_to_freq:
            combis += cumsum_to_freq[comp]
        
        cumsum_to_freq[cumsum] += 1
        

    return combis

@pytest.mark.parametrize(
    ("input_data", "k", "expected"),
    [
        [[1, 1, 1], 2, 2],
        [[1, 2, 3], 3, 2],
        [
            [3, 5, 1, 1, 2, 2, 3, 4],
            3,
            3,
        ],
    ],
)
def test_exercise(input_data, k, expected):
    assert exercise(input_data, k) == expected
