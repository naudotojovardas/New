# Function: Invert RGB Color
# Objective: Write a function `color_invert` that takes an RGB color tuple and returns the inverted color tuple.
# Parameters:
# - color: A tuple with three integers representing the RGB values of the color (each value ranges from 0 to 255).
# Returns:
# - A tuple representing the inverted RGB values.


def color_invert(color):
    inverted_color = tuple(255 - value for value in color)
    return inverted_color
color = input('Input color by words or type done: ').lower()
if color == 'done' :
    red = int(input('input the red value(0-255): '))
    green = int(input('input the green value(0-255): '))
    blue = int(input('input the blue value (0-255): '))
    color = (red, green, blue)
    inverted_color = color_invert(color)
    print(f'Inverted RGB color is: {inverted_color}')
else:
    print('wrong information, abort!')




