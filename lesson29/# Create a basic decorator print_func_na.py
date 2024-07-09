# Create a basic decorator print_func_name that prints the name of the function before it is called.

def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(f'Calling function {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@print_func_name
def foo():
    print('Inside foo')

print(foo())