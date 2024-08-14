# Adjust your solution to first lesson's exercises using parametrization.

import pytest

def left2(str):
    return str[2:] + str[:2]

@pytest.mark.parametrize("input, expected", [ ("Hello", "lloHe"), ("java", "vaja"), ("Hi", "Hi") ])

def test_left2(input, expected):
    assert left2(input) == expected



