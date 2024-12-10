from typing import List, Optional

import pytest


def exercise(n: List[int]) -> List[int]:
    """
    n
    n == 1 --> return 1
    n == 2 --> return 1 (1+combis(n-1)) + 1 (2) = 2
    n == 3 --> combis(n-1) + combis(n-2) = combis(2) + combis(1) = 3
               1-1-1, 1-2, 2-1
    n = 4 --> combis(n-1) + combis(n-2) = combis(3) + combis(2) = 5
               1-1-1-1, 1-1-2, 1-2-1, 2-1-1, 2-2
    
    """

    combis_for_n = {1: 1, 2: 2}

    for m in range(3, n + 1):
        combis_for_n[m] =combis_for_n[m-1] + combis_for_n[m-2]
    
    return combis_for_n[n]
    

@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (2, 2),
        (3, 3),
        (4, 5),
        (44, 1134903170)
    ],
)
def test_exercise(input_data, expected):
    assert exercise(input_data) == expected
