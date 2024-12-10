from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    [
        1 1 1
        2 2 0
        1 0 1
    ]

    """
    # BFS iter
    # original_color = image[sr][sc]
    # if original_color == color:
    #     return image
    # num_rows, num_cols = len(image), len(image[0])
    
    # q = [(sr, sc)]
    # visisted = set()

    # while len(q) > 0:
    #     row, col = q.pop(0)
    #     image[row][col] = color
    #     visisted.add((row, col))

    #     nbr, nbc = (row - 1, col)
    #     if row > 0 and (nbr, nbc) not in visisted and image[nbr][nbc] == original_color:
    #         q.append((nbr, nbc))

    #     nbr, nbc = (row, col - 1)
    #     if col > 0 and (nbr, nbc) not in visisted and image[nbr][nbc] == original_color:
    #         q.append((nbr, nbc))

    #     nbr, nbc = (row + 1, col)
    #     if (
    #         row < num_rows - 1
    #         and (nbr, nbc) not in visisted
    #         and image[nbr][nbc] == original_color
    #     ):
    #         q.append((nbr, nbc))

    #     nbr, nbc = (row, col + 1)
    #     if (
    #         col < num_cols - 1
    #         and (nbr, nbc) not in visisted
    #         and image[nbr][nbc] == original_color
    #     ):
    #         q.append((nbr, nbc))

    # DFS recursive
    # original_color = image[sr][sc]
    # if original_color == color:
    #     return image
    # num_rows, num_cols = len(image), len(image[0])
    # visited = set()

    # def fill(row, col):
    #     current_color = image[row][col]
    #     visited.add((row, col))
    #     if current_color != original_color:
    #         return
    #     print((row, col))
    #     image[row][col] = color

    #     for nb_row, nb_col in [
    #         (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), 
    #     ]:
    #         is_visited = (nb_row, nb_col) in visited
            # within_bounds = (0 <= nb_row < num_rows) and (0 <= nb_col < num_cols)
            #     if is_visited or not within_bounds:
            #         continue
    #         if image[nb_row][nb_col] == original_color:
    #             fill(nb_row, nb_col)

    # fill(sr, sc)

    # BFS recursive
    original_color = image[sr][sc]
    if original_color == color:
        return image
    num_rows, num_cols = len(image), len(image[0])
    visited = set()

    def fill(pixels):

        next_level = []
        for row, col in pixels:
            # fill the pixel and mark as visited
            current_color = image[row][col]
            visited.add((row, col))
            if current_color != original_color:
                continue
            print((row, col))
            image[row][col] = color

            # if pixel in original color, then add nb's for next level
            # (only if original color)
            for nb_row, nb_col in [
                (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), 
            ]:
                is_visited = (nb_row, nb_col) in visited
                within_bounds = (0 <= nb_row < num_rows) and (0 <= nb_col < num_cols)
                if is_visited or not within_bounds:
                    continue
                if image[nb_row][nb_col] == original_color:
                    next_level.append((nb_row, nb_col))
                    
        if next_level:
            fill(next_level)

    fill([(sr, sc)])

    return image


@pytest.mark.parametrize(
    ("input_data", "sr", "sc", "color", "expected"),
    [
        (
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            1,
            1,
            2,
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        (
            [[0, 0, 0], [0, 0, 0]],
            0,
            0,
            0,
            [[0, 0, 0], [0, 0, 0]],
        ),
    ],
)
def test_exercise(input_data, sr, sc, color, expected):
    assert exercise(input_data, sr, sc, color) == expected
