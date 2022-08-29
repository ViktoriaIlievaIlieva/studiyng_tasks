#
# In this task you will learn method overriding.
# 1. Create a Shape class. In this Shape class create an empty method get_area by using the pass keyword.
#
# 2. Create a Circle class that has an attribute for radius. Define the method get_area again
# but this time with the actual calculation for a cricle. This is called overriding.
#
# 3. Create a Rectangle class that has an attribute for width and one for height and also overrides the get_area method.
#
# 4. Create a Triangle class that has an attribute for side and an attribute for height and also overrides the get_area method.
#
# 5. Create a separate function print_shape_area that can take any shape
# and print out a formatted string f"The shape's area is - {area}"
#
# 6. To test it create an instance of each of the three classes and pass each of them to print_shape_area (polymorphism)
#

class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14 * self.radius ** 2

        return area


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height

        return area


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def get_area(self):
        area = self.height * self.side

        return area


def print_shape_area(shape: Shape):
    area = shape.get_area()
    print(f"The shape's area is - {area}")


circle = Circle(5)
rect = Rectangle(2, 3)
triangle = Triangle(9, 3)

print_shape_area(circle)
print_shape_area(rect)
print_shape_area(triangle)






