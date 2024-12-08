from collections import deque
from typing import List, Optional

import pytest


def exercise(grid: list[list[str]]) -> int:
    """ """
    num_islands = 0
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and grid[row][col] == "1":
                num_islands += 1
                bfs(row, col, grid, visited)
    
    return num_islands

def bfs(row, col, grid, visited):
    elem = (row, col)
    queue = deque()
    queue.append(elem)
    while queue:
        row, col = queue.popleft()
        visited.add(elem)

        # explore neighbours that are land
        # up, left, down, right
        nb = (row-1, col)
        if row > 0 and nb not in visited and grid[nb[0]][nb[1]] == "1":  # up
            queue.append(nb)
            visited.add(nb)
        
        nb = (row, col - 1)
        if col > 0  and nb not in visited and grid[nb[0]][nb[1]] == "1":  # up
            queue.append(nb)
            visited.add(nb)

        nb = (row + 1, col)
        if row < len(grid) - 1 and nb not in visited and grid[nb[0]][nb[1]] == "1":  # up
            queue.append(nb)
            visited.add(nb)

        nb = (row, col + 1)
        if col < len(grid[0]) - 1 and nb not in visited and grid[nb[0]][nb[1]] == "1":  # up
            queue.append(nb)
            visited.add(nb)
    
    return visited


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ],
)
def test_exercise(input_data, expected):
    assert exercise(input_data) == expected
