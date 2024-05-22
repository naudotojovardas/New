def longest_consecutive_sequence(nums):
    max_len = 0
    curr_len = 1

    # Sort the list in ascending order
    nums.sort()

    for i in range(1, len(nums)):
        # Check if the current number is consecutive to the previous number
        if nums[i] == nums[i - 1] + 1:
            curr_len += 1
        else:
            # If the sequence is broken, update the maximum length
            max_len = max(max_len, curr_len)
            curr_len = 1
    
    # Check if the last sequence is the longest
    max_len = max(max_len, curr_len)

    return max_len


# Ask the user to enter a list of integers
nums = list(map(int, input("Enter a list of integers (space-separated): ").split()))

# Call the function to determine the longest consecutive sequence
max_sequence_length = longest_consecutive_sequence(nums)

# Explain the result
print(f"The longest sequence of consecutive numbers in the list is: {max_sequence_length}")