from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(s: str) -> list[str]:
    """
    brute force

    a 1 b 2

    a + perms ("1 b 2")
            1 + perms(b 2)
                b + perms(2)
                    2
                B + perms(2)
                    2
    A + perms ("1 b 2")
            1 + perms(b 2)
                b + perms(2)
                    2
                B + perms(2)
                    2

    2 and call perms(idx - 1, [2])
    [b to each perms, B to each perms] and call perms(idx - 1)
    ...
    idx == 0 add perms and return

    """
    def get_permutations(idx, previous_perms):
        char = s[idx]
        perms_for_idx = [char + p for p in previous_perms]
        if char.isalpha():
            perms_for_idx += [char.swapcase() + p for p in previous_perms]

        if idx == 0:
            return perms_for_idx
        else:
            return get_permutations(idx - 1, perms_for_idx)

    perms = get_permutations(len(s) - 1, [""])
    return perms


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            "a1b2",
            ["a1b2","a1B2","A1b2","A1B2"],
        ),
        (
            "3z4",
            ["3z4","3Z4"]
        ),
    ],
)
def test_exercise(input_data, expected):
    # assert exercise(input_data) == expected
    assert set(exercise(input_data)) == set(expected)
