# We’ve done something similar before, but this time let’s create a class that takes temperature measurements in Kelvins
# and adds static methods to transform those into Celsius and Fahrenheit units.

class Temperature:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    @staticmethod
    def kelvin_to_celsius(kelvin) -> float:
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin) -> float:
        return kelvin * 9/5 - 459.67

    def __str__(self):
        return f'{self.kelvin}K'

temp = Temperature(200)
print(temp)
print(Temperature.kelvin_to_celsius(300))
print(Temperature.kelvin_to_fahrenheit(300))
