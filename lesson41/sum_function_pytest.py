# Re-implement all exercises from the previous lessons using the pytest framework.
# Don't forget to add _pytest to the file names to differentiate between the "manual" (first lesson), unittest (2nd lesson), and pytest (this lesson) versions.

import pytest

def sum_numbers(list_of_numbers: list) -> int:
    """Sum all numbers in a list."""
    return sum(list_of_numbers) if list_of_numbers else None


def test_sum_numbers():
    assert sum_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_numbers([]) == None
    assert sum_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55

