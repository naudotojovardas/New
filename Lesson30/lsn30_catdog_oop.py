# Create an abstract class Animal which takes the name of the animal as an input and initializes it.
# The create speak abstract method (will be overridden by subclasses) and get_name method which returns the name of the animal.
# Now create two subclasses of Animals: Dog and Cat which overrides the speak method, and provide the implementation which returns
# a string "Dog says Woof!" and "Cat says Meow!" respectively.

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def get_name(self):
        return self.name
    
class Dog(Animal):
    def speak(self):
        return "Dog says Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Cat says Meow!"
    
dog = Dog("Tommy")
cat = Cat("Kitty")

print(dog.get_name())
print(dog.speak())
print(cat.get_name())
print(cat.speak())

