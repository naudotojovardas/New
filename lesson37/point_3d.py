# Create an immutable data class named Point3D for representing points in a three-dimensional space.
#  The class should contain three coordinates: x, y, and z, all of which are set once upon instance creation and cannot be changed thereafter.
#  Use the concept of immutability to ensure these instances remain consistent and error-free throughout their lifecycle.

from dataclasses import dataclass

@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    def __str__(self):
        return f'Point3D(x={self.x}, y={self.y}, z={self.z})'
    
p = Point3D(1, 2, 3)
print(p)

try:
    p.x = 4
except Exception as e:
    print(e)

try:
    p.y = 5
except Exception as e:
    print(e)

try:
    p.z = 6
except Exception as e:
    print(e)

