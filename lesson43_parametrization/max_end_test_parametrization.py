 # Adjust your solution to first lesson's exercises using parametrization.

import pytest

def max_end3(nums):
    max_num = max(nums[0], nums[-1])
    return [max_num] * 3

@pytest.mark.parametrize("nums, expected", [ ([1, 2, 3], [3, 3, 3]), ([11, 5, 9], [11, 11, 11]), ([2, 11, 3], [3, 3, 3]), ([11, 3, 3],
                                              [11, 11, 11]), ([3, 11, 11], [11, 11, 11]), ([2, 2, 2], [2, 2, 2]), ([2, 11, 2], [2, 2, 2]), ([0, 0, 1], [1, 1, 1]) ])

def test_max_end3(nums, expected):
    assert max_end3(nums) == expected

