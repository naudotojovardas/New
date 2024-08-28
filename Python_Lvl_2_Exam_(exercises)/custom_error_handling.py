# Custom Error Handling
# Objective: Create a class `AgeError` as a custom exception and a function `check_age` that raises `AgeError` if age is below 18 or above 120.
# Parameters:
# - age: An integer representing a person's age.
# Returns:
# - True if the age is valid, otherwise raises `AgeError`.
# Details:
# - `AgeError` should extend from `Exception` and include an error message that indicates the invalid age range.

class AgeError(Exception):
    def __init__(self, message="Invalid age: {}. Age must be between 18 and 120"):
        self.message = message
        super().__init__(self.message)
    pass

def check_age(age):
    if age < 18 or age > 120:
        raise AgeError(message="Invalid age: {}. Age must be between 18 and 120".format(age))
    return True


# Examples:
print(check_age(25))  # Expected: True
print(check_age(17))  # Expected to raise: AgeError: Invalid age: 17. Age must be between 18 and 120
print(check_age(121)) # Expected to raise: AgeError: Invalid age: 121. Age must be between 18 and 120
