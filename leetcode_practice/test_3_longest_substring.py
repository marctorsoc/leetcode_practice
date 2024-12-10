from typing import Optional

import pytest


def lengthOfLongestSubstring(s: str) -> int:
    """
    """
    


    














    """
    a  b  c  a  b  c  b  b
       l        r             
    max=3
    {a: 0, b: 1, c: 2}

    if s[r] not in seen or lower than left, then:
        - add to map with i
        - update global_max to i - left + 1
    else
        - add to map with i
        - move left to s[r] + 1

    stop when right gets to the end
    """
    # c_to_idx = dict()
    # left, global_max = 0, 0

    # for idx, c in enumerate(s):
    #     if c not in c_to_idx or c_to_idx[c] < left:
    #         global_max = max(global_max, idx - left + 1)
    #         c_to_idx[c] = idx
    #         continue
            
    #     left = c_to_idx[c] + 1
    #     c_to_idx[c] = idx
    
    # return global_max


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("tmmzuxt", 5),
    ],
)
def test_exercise(s, expected):
    assert lengthOfLongestSubstring(s) == expected
