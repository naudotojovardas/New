# Write a Python program to square and cube every number in a given list of integers using lambda functions.

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

square = lambda x: x ** 2
cube = lambda x: x ** 3

print(list(map(square, a)))
print(list(map(cube, a)))
print(list(map(square, b)))
print(list(map(cube, b)))
print(list(map(square, c)))
print(list(map(cube, c)))




