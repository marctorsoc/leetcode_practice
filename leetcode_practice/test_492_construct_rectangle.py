from collections import defaultdict
from typing import List, Optional

import pytest


def exercise(area: int) -> list[int]:
    pass

    ############################################################

    


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (
            4,
            [2, 2],
        ),
        (
            37,
            [37, 1],
        ),
        (
            9999998,
            [4999999, 2],
        ),
    ],
    ids=[1, 2, 3],
)
def test_exercise(input_data, expected):
    assert exercise(input_data) == expected
