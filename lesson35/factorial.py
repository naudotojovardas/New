# Create a class method to return the factorial of a given number.

class Math_Factorial:
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Math_Factorial.factorial(n - 1)
        
print(Math_Factorial.factorial(5))  # Output: 120
print(Math_Factorial.factorial(6))  # Output: 720
print(Math_Factorial.factorial(7))  # Output: 5040
print(Math_Factorial.factorial(8))  # Output: 40320