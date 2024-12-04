from typing import Optional

import pytest


def lengthOfLongestSubstring(s: str) -> int:
    maxLength = 0
    start = 0
    char_to_idx = dict()

    for idx, c in enumerate(s):
        print(start, idx, maxLength, s[start:idx + 1])

        if c not in char_to_idx or char_to_idx[c] < start:
            maxLength = max(maxLength, idx - start + 1)
            char_to_idx[c] = idx
            continue
        
        start = char_to_idx[c] + 1
        char_to_idx[c] = idx
        
    return maxLength



@pytest.mark.parametrize(
    ("s", "expected"),
    [
        # ("abcabcbb", 3),
        # ("bbbbb", 1),
        # ("pwwkew", 3),
        ("tmmzuxt", 5),
    ],
)
def test_exercise(s, expected):
    assert lengthOfLongestSubstring(s) == expected
