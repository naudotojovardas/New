# Re-implement all exercises from the previous lessons using the pytest framework.
# Don't forget to add _pytest to the file names to differentiate between the "manual" (first lesson), unittest (2nd lesson), and pytest (this lesson) versions.

import pytest

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

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_prime(16) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True
    assert is_prime(20) == False
    assert is_prime(21) == False
    assert is_prime(22) == False
    assert is_prime(23) == True
    assert is_prime(24) == False
    assert is_prime(25) == False
    assert is_prime(26) == False
    assert is_prime(27) == False
    assert is_prime(28) == False
    assert is_prime(29) == True
    assert is_prime(30) == False
    assert is_prime(31) == True
    assert is_prime(32) == False
    assert is_prime(33) == False
    assert is_prime(34) == False
    assert is_prime(35) == False
    assert is_prime(36) == False
    assert is_prime(37) == True
    assert is_prime(38) == False
    assert is_prime(39) == False
    assert is_prime(40) == False
    assert is_prime(41) == True
    assert is_prime(42) == False
    assert is_prime(43) == True
    assert is_prime(44) == False
    assert is_prime(45) == False
    assert is_prime(46) == False
    assert is_prime(47) == True
    assert is_prime(48) == False
    assert is_prime(49) == False
    assert is_prime(50) == False