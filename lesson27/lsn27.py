# Python program to check if a given string starts with a specified character using a lambda function. The program should return True or False

starts_with = lambda s, char: True if s.startswith(char) else False
print(starts_with('Python', 'P'))