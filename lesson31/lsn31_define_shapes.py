# Define a Shape class with the following attributes and methods:
#   The name attribute is a string that represents the name of the shape.
#   The sides attribute is an integer that represents the number of sides of the shape.
#   An area() method returns the area of the shape.
# Then, define a Rectangle class that inherits from the Shape class and has the following attributes and methods:
#   The width attribute is a float that represents the width of the rectangle.
#   The height attribute is a float that represents the height of the rectangle.
#   An init() method that initializes the name, sides, width, and height attributes.
#   An area method that overrides the area method of the Shape class and returns the area of the rectangle.
# Finally, define a Square class that inherits from the Rectangle class and has the following attributes and methods:
#   The side_length attribute is a float that represents the length of the sides of the square.
#   An init() method that initializes the side_length attribute and calls the init method of the Rectangle class to initialize the name, sides, width, and height attributes.


class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, sides, width, height):
        super().__init__(name, sides)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

class Square(Rectangle):
    def __init__(self, name, sides, side_length):
        super().__init__(name, sides, side_length, side_length)


rectangle = Rectangle("rectangle", 4, 2, 3)
print(rectangle.area())

square = Square("square", 4, 2)
print(square.area())

