import heapq
from typing import List, Optional

import pytest


def exercise(nums: List[int], k: int) -> int:
    """
    less than O(n * logn)

    heap -> 
        - insert O(log(n))
        - find min = O(1)

    easy solution:
        - insert all into the heap: n logn
        - pop k - 1 : log(k)
        - pop one and return
        - memory is o(n)

    advanced solution
        - [3,2,1,5,6,4], k=2
          start with :k
          when a new num comes. If higher than the min,
          then either the k-1 is the kth or the new num is the kth
    
    """
    # heap = nums[:k]
    # heapq.heapify(heap)  # o(log k)

    # for num in nums:  # n * (O(1) + O(logk)) = O(n log k)
    #     current_min = heapq.heappop(heap)
    #     if num > current_min:
    #         heapq.heappush(heap, num)
    #     else:
    #         heapq.heappush(heap, current_min)

    # return heapq.heappop(heap)

    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) <= k:
            continue
        heapq.heappop(heap)

    return heapq.heappop(heap)

    

@pytest.mark.parametrize(
    ("input_data", "k", "expected"),
    [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
    ],
)
def test_exercise(input_data, k, expected):
    assert exercise(input_data, k) == expected
