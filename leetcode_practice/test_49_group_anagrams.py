from collections import defaultdict
from typing import Optional

import pytest


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    ["eat","tea","tan","ate","nat","bat"]
    """
    key_to_anagrams = defaultdict(list)
    for cur in strs:
        key = sorted(cur)
        key_to_anagrams[tuple(key)].append(cur)

    return [sorted(group) for group in key_to_anagrams.values()]

@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            ["eat","tea","tan","ate","nat","bat"],
            [["bat"],["nat","tan"],["ate","eat","tea"]],
        ),
        (
            [""],
            [[""]],
        ),
        (
            ["a"],
            [["a"]],
        ),
        (
            ["","",""],
            [["","",""]],
        )
    ],
)
def test_exercise(input_data, expected):
    # assert groupAnagrams(input_data) == expected
    assert sorted(groupAnagrams(input_data), key=lambda t: t[0]) == sorted(expected, key=lambda t: t[0])
