# In this file create a class Rectangle
# In the Rectangle add the attributes width and height (taking them in the constructor)
# Create a function get_area() for Rectangle that calculates its area and RETURNs it (width * height)
# Create a function get_perimeter() for Rectangle that calculates its perimeter and RETURNs it (2 * (width + height))
# Create a function is_square() for Rectangle that checks if width is equal to height and RETURNs True if they are and False if they are not

# Ask the user for width
# Ask the user for height

# Create a variable of type rectangle
# Print the rectangle area
# Print the rectangle perimeter
# if the rectangle is a square print "Rectangle is a square"

class Rectangle:
    def __init__(self,width, height ):
        self.width = width
        self.height = height

    def get_area(self):
        get_area = self.width * self.height
        return get_area

    def get_perimeter(self):
        get_perimeter = 2 * (self.width + self.height)
        return get_perimeter

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

width = int (input ("Insert width:"))
height = int (input ("Insert height:"))

rectangle = Rectangle (width, height)

my_rectangle_area= rectangle.get_area()
print (my_rectangle_area)

my_rectangle_perimeter= rectangle.get_perimeter()
print (my_rectangle_perimeter)

equal_sides = rectangle.is_square()
if equal_sides == True:
    print ("Rectangle is a square")

#DONE