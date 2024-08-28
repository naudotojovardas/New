# Multiply all the values in a given list of integers.

def multiply_list(items):
    result = 1
    for x in items:
        result *= x
    return result

print(multiply_list([1, 2, 3, 4, ]))