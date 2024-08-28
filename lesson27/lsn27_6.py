# Write a Python program to sort a list of dictionaries by the color key using a lambda function.

lst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 
'Blue'}]

print(sorted(lst, key = lambda x: x['color']))
