from typing import Optional

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    pass















    #############################





    # preamble = ListNode() # we will return next of this
    # result = preamble
    # carry = 0

    # while l1 is not None or l2 is not None or carry:

    #     # compute val and carry
    #     a = l1.val if l1 else 0
    #     b = l2.val if l2 else 0
    #     val = a + b + carry
    #     carry = int(val > 9)

    #     # save to result
    #     result.next = ListNode(val % 10)
    #     result = result.next

    #     l1 = l1.next if l1 else None
    #     l2 = l2.next if l2 else None


    # return preamble.next


# @pytest.mark.parametrize(
#     ("nums", "target", "expected"),
#     [
#         ([2, 7, 11, 15], 9, [0, 1]),
#         ([3, 2, 4], 6, [1, 2]),
#         ([3, 3], 6, [0, 1]),
#     ],
# )
# def test_twoSum(nums, target, expected):
#     assert twoSum(nums, target) == expected
