# Write 5 tests for it. 
# After running your tests, do you notice a bug in the function?
# Fix the function and re-run your tests.
# Write tests for making sure that the function raises TypeError if not all elements in the argument are numbers

def sum_numbers(list_of_numbers: list) -> int:
    """Sum all numbers in a list."""
    return sum(list_of_numbers) if list_of_numbers else None

def test_sum_numbers():
    assert sum_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_numbers([5, 4, -3, 2, 1]) == 9
    assert sum_numbers([-1, -2, -3, -5, -4]) == -15
    assert sum_numbers([1, 2, 5, 5, 4]) == 17
    assert sum_numbers([1, 5, 2, -3, 4]) == 9
    assert sum_numbers([5, 1, 2, 3, 4]) == 15
    assert sum_numbers([1, 1, 1, 1, 1]) == 5
    assert sum_numbers([1]) == 1
    assert sum_numbers([]) == None
    return "All tests passed"

print(test_sum_numbers())