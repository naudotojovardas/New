# Adjust your solution to first lesson's exercises using parametrization.

import pytest

def first_two(str):
    return str[:2]

@pytest.mark.parametrize("input, expected", [ ("Hello", "He"), ("abcdef", "ab"), ("ab", "ab"), ("a", "a"), ("", "") ])

def test_first_two(input, expected):
    assert first_two(input) == expected

