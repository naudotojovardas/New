class person():
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
    def greet(self):
        print(f"hello, {self.name} {self.surname}!")
name_surname = person("first", "person")
name_surname.greet()