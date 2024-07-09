# Create a simple Circle class with a private radius attribute. Provide methods for setting and getting the radius, ensuring the radius cannot be negative.

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def area(self):
        return 3.14159 * self.__radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.__radius}"
    
c = Circle(5)
print(c)