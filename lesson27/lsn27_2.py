# Create two lambda functions: one that adds 15 to a given number, and another that multiplies two arguments, x and y. Print the results of both functions.

add_15 = lambda x: x + 15
multiply = lambda x, y: x * y

print(add_15(10))
print(multiply(2, 3))