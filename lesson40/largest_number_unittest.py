# Re-implement all exercises from the previous lesson using the unittest framework.
#  Don't forget to add _unittest to the file names to differentiate between the "manual" (first lesson) and unittest (this lesson) versions.

import unittest

def find_largest_number(numbers: list) -> float:
    """Finds the largest number in a list of numbers."""
    if not numbers:
        return None

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest

# def test_find_largest_number():
#     assert find_largest_number([1, 2, 3, 4.0, 5]) == 5
#     assert find_largest_number([5, 4, -3, 2, 1]) == 5
#     assert find_largest_number([-1, -2, -3, -5, -4]) == -1
#     assert find_largest_number([1, 2, 5, 5, 4]) == 5
#     assert find_largest_number([1, 5, 2, -3.0, 4]) == 5.0
#     assert find_largest_number([5, 1, 2, 3, 4]) == 5
#     assert find_largest_number([1, 1, 1, 1, 1]) == 1
#     assert find_largest_number([1]) == 1
#     assert find_largest_number([]) == None
#     return "All tests passed"


class TestFindLargestNumber(unittest.TestCase):
    def test_find_largest_number(self):
        self.assertEqual(find_largest_number([1, 2, 3, 4.0, 5]), 5)
        self.assertEqual(find_largest_number([5, 4, -3, 2, 1]), 5)
        self.assertEqual(find_largest_number([-1, -2, -3, -5, -4]), -1)
        self.assertEqual(find_largest_number([1, 2, 5, 5, 4]), 5)
        self.assertEqual(find_largest_number([1, 5, 2, -3.0, 4]), 5.0)
        self.assertEqual(find_largest_number([5, 1, 2, 3, 4]), 5)
        self.assertEqual(find_largest_number([1, 1, 1, 1, 1]), 1)
        self.assertEqual(find_largest_number([1]), 1)
        self.assertEqual(find_largest_number([]), None)

if __name__ == "__main__":
    unittest.main()


# print(test_find_largest_number())