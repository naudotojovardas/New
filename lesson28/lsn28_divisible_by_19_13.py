# Write a Python program to find numbers divisible by 19 or 13 from a list using Lambda.

def divisible_by_19_or_13(nums):
    return list(filter(lambda x: x % 19 == 0 or x % 13 == 0, nums))

def main():
    nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
    print(divisible_by_19_or_13(nums))

main()