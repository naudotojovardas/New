# Implement a Timer Decorator
# Objective: Write a decorator `timer` that measures the execution time of any function it decorates.
# Parameters:
# - None directly; it decorates functions.
# Returns:
# - Wrapper function that prints the execution time.
# Details:
# - Use the `time` module to calculate the execution time.
# - Print the time in seconds.

import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print(f"Function `{func.__name__}` took {end - start:.3f} seconds")
	return wrapper
	pass

# Desired Outcome:
@timer
def some_heavy_computation():
	for i in range(1000000):
		pass
	time.sleep(2)
some_heavy_computation()  # Expected to print: Function `some_heavy_computation` took X.XXX seconds


