# Concatenate all strings in a list.

import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@time_execution
def example_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(example_function(1000000))