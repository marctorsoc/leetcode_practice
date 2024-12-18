from typing import List, Optional

import pytest


def exercise(version1: str, version2: str) -> int:
    """ 
    """





















    #######################################################

    """
    16313.2.324
    a

    1
    10 + 6 = 16
    160 + 3 = 163
    1630 + 1 = 1631
    16310 + 3 = 16313

    15.10.03
    b

    start with pointers in first char, then move together
    once we find a . in one of the two, then keep moving the other one until finding a .
    at that point, we can compare revisions. If they're different then we can return
    
    once we find a number, we multiply the previous thing by 10       

    """

    a, b = 0, 0
    revision1, revision2 = 0, 0
    print(version1, version2)
    while a < len(version1) or b < len(version2):
        a_end_of_revision = a >= len(version1) or version1[a] == "."
        b_end_of_revision = b >= len(version2) or version2[b] == "."

        if not a_end_of_revision:
            revision1 = revision1 * 10 + int(version1[a])
            a += 1
        if not b_end_of_revision:
            revision2 = revision2 * 10 + int(version2[b])
            b += 1

        if a_end_of_revision and b_end_of_revision:
            if revision1 != revision2:
                return -1 if revision1 < revision2 else 1

            revision1 = revision2 = 0
            a += 1
            b += 1

    if revision1 < revision2:
        return -1
    elif revision1 > revision2:
        return 1
    return 0


@pytest.mark.parametrize(
    ("input_data", "version2", "expected"),
    [
        [
            "1.2",
            "1.10",
            -1,
        ],
        [
            "1.01",
            "1.001",
            0,
        ],
        [
            "1.0",
            "1.0.0.0",
            0,
        ],
        [
            "1.0.1",
            "1",
            1,
        ],
    ],
)
def test_exercise(input_data, version2, expected):
    assert exercise(input_data, version2) == expected
