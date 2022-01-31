from dataclasses import dataclass
import math


@dataclass
class Circle:
    radius: float
    center_position: tuple

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius


@dataclass
class Rectangle:
    length: float
    width: float
    top_left_corner_position: tuple

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (2 * self.length) + (2 * self.width)