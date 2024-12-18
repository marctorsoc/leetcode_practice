import functools
from typing import List, Optional

import pytest


def exercise(n: int, k: int) -> List[List[int]]:
    """ """
    pass









    #######################################################

    """
    4,2,
    len(nums) - 1 = 3
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],

    current = [1]
    result = []
    nums = [1, 2, 3, 4]
    
    start = 1


    """

    # with append outside of the loop (traditional way)
    current, result = [], []

    def backtrack(start):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, n):
            current.append(i + 1)
            backtrack(i + 1)
            current.pop()

    # print(result)


    # with append inside of the loop
    # current = []
    # result = []

    # def backtrack(start):
    #     for i in range(start, n):
    #         num = i + 1
    #         current.append(num)
    #         if len(current) == k:
    #             result.append(current[:])
    #         elif num < n:
    #             backtrack(num)
    #         current.pop()

    backtrack(0)
    return result


@pytest.mark.parametrize(
    ("input_data", "k", "expected"),
    [
        (
            4,
            2,
            [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
        ),
        (
            1,
            1,
            [[1]],
        ),
        (
            5,
            3,
            [
                [1, 2, 3],
                [1, 2, 4],
                [1, 2, 5],
                [1, 3, 4],
                [1, 3, 5],
                [1, 4, 5],
                [2, 3, 4],
                [2, 3, 5],
                [2, 4, 5],
                [3, 4, 5],
            ],
        ),
    ],
    ids=[1, 2, 3],
)
def test_exercise(input_data, k, expected):
    # print(expected)
    assert sorted(exercise(input_data, k)) == sorted(expected)
