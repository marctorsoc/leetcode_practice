from dataclasses import dataclass
from typing import List, Optional

import pytest


@dataclass
class Node:
    start: int
    end: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class MyCalendar:

    def __init__(self):
        self.tree = None

    def book(self, startTime: int, endTime: int) -> bool:
        newNode = Node(start=startTime, end=endTime)
        if not self.tree:
            self.tree = newNode
            return True

        return self.insert(self.tree, newNode)

    def insert(self, node, newNode):
        print()
        print(node)
        print(newNode)
        import pdb; pdb.set_trace()
        if node.end < newNode.start:
            if node.right:
                return self.insert(node.right, newNode)
            else:
                node.right = newNode
                return True
        elif node.start > newNode.end:
            if node.left:
                return self.insert(node.left, newNode)
            else:
                node.left = newNode
                return True
        return False

    ############################################################


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            [[10, 20], [15, 25], [20, 30]],
            [True, False, True],
        ),
        # (
        #     37,
        #     [37, 1],
        # ),
    ],
    # ids=[1, 2, 3],
)
def test_exercise(input_data, expected):
    calendar = MyCalendar()
    for event, e in zip(input_data, expected):
        assert calendar.book(*event) == e
