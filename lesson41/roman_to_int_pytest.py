# Think about various cases how to test and break this function
# Write at least 10 tests for this function
# Think about what exceptions should be thrown in this function in order to improve its usage
# Implement tests using pytest for these exceptions

import pytest

def roman_to_int(roman_num: str) -> int:
  """Converts a basic Roman numeral string (I, V, X, L, C) to an integer (limited to values up to 3999)."""
  roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000}
  total = 0
  prev_val = 0
  for char in roman_num:
    val = roman_map[char]
    total += val
    # Handle subtractive notation (e.g., IV, IX)
    if prev_val < val and prev_val in (1, 10, 100):
      total -= 2 * prev_val
    prev_val = val
  return total

def test_roman_to_int():
  assert roman_to_int("I") == 1
  assert roman_to_int("V") == 5
  assert roman_to_int("X") == 10
  assert roman_to_int("L") == 50
  assert roman_to_int("C") == 100
  assert roman_to_int("D") == 500
  assert roman_to_int("M") == 1000
  assert roman_to_int("IV") == 4
  assert roman_to_int("IX") == 9
  assert roman_to_int("XL") == 40
  assert roman_to_int("XC") == 90
  assert roman_to_int("CD") == 400
  assert roman_to_int("CM") == 900
  assert roman_to_int("MMXVIII") == 2018
  assert roman_to_int("MMMCMXCIX") == 3999

# def test_roman_to_int_exceptions():
#   with pytest.raises(ValueError):
#     roman_to_int("A")
#   with pytest.raises(ValueError):
#     roman_to_int("IIII")
#   with pytest.raises(ValueError):
#     roman_to_int("VV")
#   with pytest.raises(ValueError):
#     roman_to_int("XXXX")
#   with pytest.raises(ValueError):
#     roman_to_int("LL")
#   with pytest.raises(ValueError):
#     roman_to_int("CC")

# print(roman_to_int("XXXVIII"))