# Objective: Fix a function `remove_empty_arrays`. It should correctly remove all empty lists from a mixed list that can contain various data types including integers, strings, and lists.
# This function should correctly handle and preserve the elements of the array that are not lists, while only removing lists that are empty.
# Parameters:
# - arr: A list containing mixed data types.
# Returns:
# - A list where all empty lists have been removed.

def remove_empty_arrays(arr):
    return [number for number in arr if not (isinstance(number, list)) and len(arr) != 0]

# Desired Outcome:
# Fix the function, so it returns the list without any empty lists while preserving other elements without any error.
arr = ([1, 2, [], 4])  #➞ [1, 2, 4]
print(remove_empty_arrays(arr))

# However, currently it throws an error:
# ERROR: Traceback:
#    in <module>
#    in remove_empty_arrays
#    in <listcomp>
# TypeError: object of type 'int' has no len()