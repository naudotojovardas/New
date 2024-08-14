# Adjust your solution to first lesson's exercises using parametrization.

import pytest

def sorta_sum(a, b):
    if 10 <= a + b <= 19 or 11<= a + b <=18 or 12<= a + b <=17 or 13<= a + b <=16 or 14<= a + b <=15:
        return 20
    else:
        return a + b
    

@pytest.mark.parametrize('a, b, expected', [ (3, 4, 7), (9, 4, 20), (10, 11, 21), (12, 13, 25), (14, 15, 20), (16, 17, 20), (18, 19, 20) ])

def test_sorta_sum(a, b, expected):
    assert sorta_sum(a, b) == expected

