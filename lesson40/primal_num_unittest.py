# Read on Wikipedia about primal numbers to get ideas what to test for
# Think about various cases how to test and break this function
# Write at least 10 tests for this function
# Think about what exceptions should be thrown in this function
# Implement tests using unittest for these exceptions

import unittest

def is_prime(num: int) -> bool:
    """Checks if a number is prime (greater than 1 and only divisible by 1 and itself)."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

class TestPrimes(unittest.TestCase):
    def test_1(self):
        self.assertFalse(is_prime(1))

    def test_2(self):
        self.assertTrue(is_prime(2))

    def test_3(self):
        self.assertTrue(is_prime(3))

    def test_4(self):
        self.assertFalse(is_prime(4))

    def test_5(self):
        self.assertTrue(is_prime(5))

    def test_6(self):
        self.assertFalse(is_prime(6))

    def test_7(self):
        self.assertTrue(is_prime(7))

    def test_8(self):
        self.assertFalse(is_prime(8))

    def test_9(self):
        self.assertFalse(is_prime(9))

    def test_10(self):
        self.assertTrue(is_prime(11))

if __name__ == '__main__':
    unittest.main()