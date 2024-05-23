# Function: Check Inequality Correctness
# Objective: Write a function `correct_signs` that evaluates an inequality expression string and returns True if the inequality holds and False otherwise.
# Parameters:
# - expression: A string containing a sequence of integers and inequality operators (e.g., <, >).
# Returns:
# - True if the inequality expression is correct, False otherwise.


# Example usages:
print(correct_signs("3 < 7 < 11"))  # ➞ True
print(correct_signs("13 > 44 > 33 > 1"))  # ➞ False
print(correct_signs("1 < 2 < 6 < 9 > 3"))  # ➞ True
