# Write a decorator uppercase_decorator that modifies the return value of any function that returns a string, making it uppercase.

def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())