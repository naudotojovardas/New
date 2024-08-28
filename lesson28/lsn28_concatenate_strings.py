# Concatenate all strings in a list.

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(["Hello", "World", "From", "Python"]))