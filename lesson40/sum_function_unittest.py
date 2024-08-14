# Re-implement all exercises from the previous lesson using the unittest framework.
#  Don't forget to add _unittest to the file names to differentiate between the "manual" (first lesson) and unittest (this lesson) versions.

import unittest

def sum_numbers(list_of_numbers: list) -> int:
    """Sum all numbers in a list."""
    return sum(list_of_numbers) if list_of_numbers else None

# def test_sum_numbers():
#     assert sum_numbers([1, 2, 3, 4, 5]) == 15
#     assert sum_numbers([5, 4, -3, 2, 1]) == 9
#     assert sum_numbers([-1, -2, -3, -5, -4]) == -15
#     assert sum_numbers([1, 2, 5, 5, 4]) == 17
#     assert sum_numbers([1, 5, 2, -3, 4]) == 9
#     assert sum_numbers([5, 1, 2, 3, 4]) == 15
#     assert sum_numbers([1, 1, 1, 1, 1]) == 5
#     assert sum_numbers([1]) == 1
#     assert sum_numbers([]) == None
#     return "All tests passed"

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([5, 4, -3, 2, 1]), 9)
        self.assertEqual(sum_numbers([-1, -2, -3, -5, -4]), -15)
        self.assertEqual(sum_numbers([1, 2, 5, 5, 4]), 17)
        self.assertEqual(sum_numbers([1, 5, 2, -3, 4]), 9)
        self.assertEqual(sum_numbers([5, 1, 2, 3, 4]), 15)
        self.assertEqual(sum_numbers([1, 1, 1, 1, 1]), 5)
        self.assertEqual(sum_numbers([1]), 1)
        self.assertEqual(sum_numbers([]), None)


if __name__ == "__main__":
    unittest.main()





# print(test_sum_numbers())