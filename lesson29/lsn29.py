# Write a Python program to square and cube every number in a given list of integers using lambda functions.

def square_cube_list(nums):
    square = list(map(lambda x: x ** 2, nums))
    cube = list(map(lambda x: x ** 3, nums))
    return square, cube


def main():
    nums = [1, 2, 3, 4, 5]
    print(square_cube_list(nums))

main()
