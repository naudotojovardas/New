# Write a Python program to sort a given matrix in ascending order based on the sum of its rows using a lambda function.

matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Original Matrix:")
print(matrix)
matrix.sort(key=lambda x: sum(x))
print("\nSort the said matrix in ascending order based on the sum of its rows:")
print(matrix)
