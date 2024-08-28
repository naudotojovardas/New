# As per previous examples please create an example of your own. The abstract class should contain five 
# (3 abstract and 2 normal) methods. Create 2 subclasses that would inherit the abstract class.

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def make_sound(self):
        print("Animal makes sound")

    def reproduce(self):
        print("Animal reproduces")

class Dog(Animal):
    def eat(self):
        print("Dog eats")

    def sleep(self):
        print("Dog sleeps")

    def move(self):
        print("Dog moves")

class Cat(Animal):
    def eat(self):
        print("Cat eats")

    def sleep(self):
        print("Cat sleeps")

    def move(self):
        print("Cat moves")

dog = Dog()
dog.eat()
dog.sleep()
dog.move()
dog.make_sound()
dog.reproduce()

cat = Cat()
cat.eat()
cat.sleep()
cat.move()
cat.make_sound()
cat.reproduce()

