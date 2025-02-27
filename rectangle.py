class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return f"Area = {self.length * self.width}"
    def perimeter(self):
        return f"Perimeter = {2*(self.length+self.width)}"
my_rectangle = Rectangle(20,10)
print(my_rectangle.area())
print(my_rectangle.perimeter())
