import pytest


def twoSum(nums: list[int], target: int) -> list[int]:
    num_to_index = dict()
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], idx]
        num_to_index[num] = idx


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_twoSum(nums, target, expected):
    assert twoSum(nums, target) == expected
