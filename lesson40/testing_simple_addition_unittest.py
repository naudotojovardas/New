# Re-implement all exercises from the previous lesson using the unittest framework. 
# Don't forget to add _unittest to the file names to differentiate between the "manual" (first lesson) and unittest (this lesson) versions.

import unittest

def sum_of_three_ints(a: int, b: int, c: int) -> int:
    return a + b + c

# def test_add():
    # try: 
        # assert sum_of_three_ints(1, 2, 3) == 6
        # assert sum_of_three_ints(1, 2, -3) == 0
        # assert sum_of_three_ints(1, -2, -3) == -4
        # assert sum_of_three_ints(-1, -2, -3) == -6
        # assert sum_of_three_ints(0, 0, 0) == 0
        # assert sum_of_three_ints(0, 0, 1) == 1
        # assert sum_of_three_ints(1054875156, 1, 9878465498498) == 9879520373655
    #     assert sum_of_three_ints(0, 1, c) == 1
    #     assert sum_of_three_ints(1, 0) == 1
    # except TypeError as e:
    #     return f'error: {e}'
    # except NameError as e:
    #     return f'error: {e}'
    # else:
        # return "All tests passed"

# Run the test
# print(test_add())

class TestSumOfThreeInts(unittest.TestCase):
    def test_sum_of_three_ints(self):
        self.assertEqual(sum_of_three_ints(1, 2, 3), 6)
        self.assertEqual(sum_of_three_ints(1, 2, -3), 0)
        self.assertEqual(sum_of_three_ints(1, -2, -3), -4)
        self.assertEqual(sum_of_three_ints(-1, -2, -3), -6)
        self.assertEqual(sum_of_three_ints(0, 0, 0), 0)
        self.assertEqual(sum_of_three_ints(0, 0, 1), 1)
        self.assertEqual(sum_of_three_ints(1054875156, 1, 9878465498498), 9879520373655)
        # with self.assertRaises(TypeError):
        #     sum_of_three_ints(0, 1, c)
        # with self.assertRaises(TypeError):
        #     sum_of_three_ints(1, 0)

if __name__ == '__main__':
    unittest.main()

