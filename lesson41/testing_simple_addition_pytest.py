# Re-implement all exercises from the previous lessons using the pytest framework.
# Don't forget to add _pytest to the file names to differentiate between the "manual" (first lesson), unittest (2nd lesson), and pytest (this lesson) versions.

import pytest

def sum_of_three_ints(a: int, b: int, c: int) -> int:
    return a + b + c

def test_sum_of_three_ints():
    assert sum_of_three_ints(1, 2, 3) == 6
    assert sum_of_three_ints(0, 0, 0) == 0
    assert sum_of_three_ints(-1, -2, -3) == -6
    assert sum_of_three_ints(1, 2, -3) == 0

def test_sum_of_three_ints_fail():
    with pytest.raises(AssertionError):
        assert sum_of_three_ints(1, 2, 3) == 7
        assert sum_of_three_ints(0, 0, 0) == 1
        assert sum_of_three_ints(-1, -2, -3) == 6
        assert sum_of_three_ints(1, 2, -3) == 1

def test_sum_of_three_ints_type():
    with pytest.raises(TypeError):
        assert sum_of_three_ints(1, 2, "3")
        assert sum_of_three_ints(1, "2", 3)
        assert sum_of_three_ints("1", 2, 3)