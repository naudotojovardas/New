# Write a decorator time_execution that measures and prints the time it takes for any function it decorates to execute.

import time 

def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper  

@time_execution
def test():
    time.sleep(2)
    return "Hello"

print(test())