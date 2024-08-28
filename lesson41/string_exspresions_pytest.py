# Think about various cases how to test and break this function
# Write at least 10 tests for this function
# Think about what exceptions should be thrown in this function in order to improve its usage
# Implement tests using pytest for these exceptions

import pytest

def is_balanced(expression: str) -> bool:
  """Checks if a string expression has balanced parentheses ((), [], {})."""
  stack = []
  mapping = {")": "(", "]": "[", "}": "{"}
  for char in expression:
    if char in mapping.values():
      stack.append(char)
    elif char in mapping:
      if not stack or stack.pop() != mapping[char]:
        return False

  return not stack

def test_is_balanced():
  assert is_balanced("()") == True
  assert is_balanced("[]") == True
  assert is_balanced("{}") == True

assert is_balanced("()[]{}") == True
assert is_balanced("([{}])") == True
assert is_balanced("([]{})") == True
assert is_balanced("({[]})") == True
assert is_balanced("({}(") == False