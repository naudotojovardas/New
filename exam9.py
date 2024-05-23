# Function: Censor Text
# Objective: Create a function `censor_text` that censors specific words in a given string by replacing them with a specified character, repeated to match the length of the censored word.
# Parameters:
# - txt: The string where the text will be censored.
# - lst: A list of words that should be censored in the string.
# - char: The character used to replace the censored words.
# Returns:
# - A string with the specified words censored.


# Example usage:
# print(censor_text("hello there, how are you doing today?", ["hello", "today"], "*"))  # Output: "***** there, how are you doing *****?"
# print(censor_text("It is very sunny outside, perfect day for a picnic", ["sunny", "picnic"], "#"))  # Output: "It is very ##### outside, perfect day for a ######"
