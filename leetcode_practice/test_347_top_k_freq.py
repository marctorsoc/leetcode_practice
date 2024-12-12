import heapq
from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(nums: list[int], k: int) -> list[int]:
    """
    [5,2,5,3,5,3,1,1,3], 2, [3, 5]
    must be lower than o(n * logn)

    5  2  5  3  5  3  1  1  3

    map   num -> freq  ....  o(n)  {5: 3, 2: 1: 3: 3, 1: 2}
    heap of size k     ....  o(n * logk)  [(5,3), (3, 3)]
    for range(k) pop   ....  o(k)

    total                    o(n * log k)
    """
    num_to_freq = defaultdict(int)
    for num in nums:
        num_to_freq[num] += 1

    heap = []
    print(num_to_freq)
    for num, freq in num_to_freq.items():
        print(heap)
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
            continue
        heapq.heappushpop(heap, (freq, num))

    return [heapq.heappop(heap)[1] for _ in range(k)]



@pytest.mark.parametrize(
    ("input_data", "target", "expected"),
    [
        (
            [1,1,1,2,2,3], 2, [1, 2]
        ),
        (
            [1], 1, [1]
        ),
        (
            [5,2,5,3,5,3,1,1,3], 2, [3, 5]
        )
    ],
)
def test_exercise(input_data, target, expected):
    # assert exercise(input_data, target) == expected
    assert set(exercise(input_data, target)) == set(expected)
