# Triple all numbers in a given list of integers using the map() function.

def triple_all(nums):
    return list(map(lambda x: x * 3, nums))

print(triple_all([1, 2, 3, 4, 5]))
print(triple_all([-1, -2, -3, -4, -5]))
print(triple_all([0, 0, 0, 0, 0]))