import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius
my_circle = Circle(4)
print(my_circle.get_area())
print(my_circle.get_circumference())