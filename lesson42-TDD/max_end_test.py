# Write tests and implement the function using the following description:
# Given an array of integers of length 3, figure out which is larger, the first or last element in the array,
# and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
    max_num = max(nums[0], nums[-1])
    return [max_num] * 3

def test():
    assert max_end3([1, 2, 3]) == [3, 3, 3]
    assert max_end3([11, 5, 9]) == [11, 11, 11]
    assert max_end3([2, 11, 3]) == [3, 3, 3]
    assert max_end3([11, 3, 3]) == [11, 11, 11]
    assert max_end3([3, 11, 11]) == [11, 11, 11]
    assert max_end3([2, 2, 2]) == [2, 2, 2]
    return('all a okey;)')

print(test())