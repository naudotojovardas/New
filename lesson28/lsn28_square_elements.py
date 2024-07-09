# Square the elements of a list using the map() function.

def square(x):
    return x ** 2

def main():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    print(squared_numbers)

main()