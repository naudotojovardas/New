# Create a class Person that has two methods:
# set_name and set_age, which set the name and age attributes of the class, respectively. Modify these methods to return self, so that the calls can be chained together.

class Person:
    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
person = Person()
print(person.set_name("John").set_age(30)) 