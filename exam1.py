# Part 1: Calculate Average Age of Users
# Objective: Write a function `calculate_average_age` that takes an array of user objects and returns
# the average age of all users as a numeric value.
# Details:
# - The function should compute the average of the 'age' values for all user objects within the provided array.
# - The result should be rounded to two decimal places if necessary.
def calculate_average_age(users):
    average_age = 0
    num_users = len(users)
    for user in users:
        average_age += user['age']
    
    average_age = average_age / num_users
    
    return round(average_age, 2)
    # Example function body (implementation needed)
    pass

# Part 2: Retrieve Sorted List of User Names
# Objective: Create a function `list_user_names` that takes an array of user objects and returns a list
# of user names sorted in alphabetical order.
# Details:
# - The function should extract the 'name' from each user object and compile a list of these names.
# - The list should be returned in alphabetical order.
def list_user_names(users):
    names = [user['name'] for user in users]
    sorted_names = sorted(names)
    return sorted_names
  
    pass

# Example user data
users = [
    {"id": '1', "name": 'John Smith', "age": 20},
    {"id": '2', "name": 'Ann Smith', "age": 24},
    {"id": '3', "name": 'Tom Jones', "age": 31},
    {"id": '4', "name": 'Rose Peterson', "age": 17},
    {"id": '5', "name": 'Alex John', "age": 25},
    {"id": '6', "name": 'Ronald Jones', "age": 63},
    {"id": '7', "name": 'Elton Smith', "age": 16},
    {"id": '8', "name": 'Simon Peterson', "age": 30},
    {"id": '9', "name": 'Daniel Cane', "age": 51},
]

# Testing the functions
print(calculate_average_age(users))  # This should print the average age
print('---')
print(list_user_names(users))  # This should print the sorted list of names
