# Create a class Animal with a method speak that prints "Animal can't speak"
# Create a class Dogs that inherits from Animals and overrides the speak method to print "Woof woof"
# Create a class Cats that inherits from Animals and overrides the speak method. 
# But in this new method call the speak method from the Animals class using the super() function, after that print "Meow meow"

# MY MODS: PRACTICE DECORATORS
# Modify the Animals class to use a decorator to print "---------------" before and after the message "Animal can't speak"
# Modify the Dogs and Cats classes to use the decorator to print the message "Animal can't speak" before and after the message "Woof woof" and "Meow meow" respectively
# Create an instance of the Dogs, Cats and Animals class and call the speak method on each one of them

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 15)
        func(*args, **kwargs)
        print("-" * 15)
    return wrapper

class Animals:
    @decorator
    def speak(self):
        print("Animal can't speak")

class Dogs(Animals):
    @decorator
    def speak(self):
        print("Woof woof")

class Cats(Animals):
    @decorator
    def speak(self):
        super().speak()
        print("Meow meow")

dog = Dogs()
cat = Cats()
animal = Animals()

dog.speak()
cat.speak()
animal.speak()