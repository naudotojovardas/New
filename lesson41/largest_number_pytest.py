# Re-implement all exercises from the previous lessons using the pytest framework.
# Don't forget to add _pytest to the file names to differentiate between the "manual" (first lesson), unittest (2nd lesson), and pytest (this lesson) versions.

import pytest

def find_largest_number(numbers: list) -> float:
    """Finds the largest number in a list of numbers."""
    if not numbers:
        return None

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest

def test_find_largest_number():
    assert find_largest_number([1, 2, 3, 4, 5]) == 5
    assert find_largest_number([5, 4, 3, 2, 1]) == 5
    assert find_largest_number([1, 2, 3, 5, 4]) == 5
    assert find_largest_number([1, 2, 3, 4, 5, 5]) == 5
    assert find_largest_number([1, 2, 3, 4, 5, 5.1]) == 5.1
    assert find_largest_number([1, 2, 3, 4, 5, 5.1, 5.2]) == 5.2
    assert find_largest_number([1, 2, 3, 4, 5, 5.1, 5.2, 5.3]) == 5.3
    assert find_largest_number([1]) == 1
    assert find_largest_number([]) == None

def test_find_largest_number_empty():
    assert find_largest_number([]) == None

def test_find_largest_number_single():
    assert find_largest_number([1]) == 1

def test_find_largest_number_multiple():
    assert find_largest_number([1, 2, 3, 4, 5]) == 5
    assert find_largest_number([5, 4, 3, 2, 1]) == 5
    assert find_largest_number([1, 2, 3, 5, 4]) == 5
    assert find_largest_number([1, 2, 3, 4, 5, 5]) == 5
    assert find_largest_number([1, 2, 3, 4, 5, 5.1]) == 5.1
    assert find_largest_number([1, 2, 3, 4, 5, 5.1, 5.2]) == 5.2
    assert find_largest_number([1, 2, 3, 4, 5, 5.1, 5.2, 5.3]) == 5.3


def test_find_largest_number_negative():
    assert find_largest_number([-1, -2, -3, -4, -5]) == -1
    assert find_largest_number([-5, -4, -3, -2, -1]) == -1
    assert find_largest_number([-1, -2, -3, -5, -4]) == -1
    assert find_largest_number([-1, -2, -3, -4, -5, -5]) == -1
    assert find_largest_number([-1, -2, -3, -4, -5, -5.1]) == -1
    assert find_largest_number([-1, -2, -3, -4, -5, -5.1, -5.2]) == -1
    assert find_largest_number([-1, -2, -3, -4, -5, -5.1, -5.2, -5.3]) == -1
    assert find_largest_number([-1]) == -1

def test_find_largest_number_mixed():
    assert find_largest_number([-1, 2, -3, 4, -5]) == 4
    assert find_largest_number([5, -4, 3, -2, 1]) == 5
    assert find_largest_number([-1, 2, -3, 5, -4]) == 5
    assert find_largest_number([-1, 2, -3, 4, 5, 5]) == 5
    assert find_largest_number([-1, 2, -3, 4, 5, 5.1]) == 5.1
    assert find_largest_number([-1, 2, -3, 4, 5, 5.1, 5.2]) == 5.2
    assert find_largest_number([-1, 2, -3, 4, 5, 5.1, 5.2, 5.3]) == 5.3
    assert find_largest_number([-1]) == -1

