#
# We need to create the following classes for our ui:
#
# Button:
# - Has x and y positio n.
# # - Has width and height.
# # - Has text for inside thebutton.
# - Has a field for storing the background color of the button.
#
# Label:
# - Has x and y position.
# - Has text for the label
#
# Both of them should inherit a class named UIElement.
# As a best practice put all repeating attributes in the UIElement class.
#
# Both of them should have their own __repr__ method in which they return a formatted string with all their information.
#
# Create an instance of a button and an instance of a label. Print each of them.
#

class UIElement:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text


class Label(UIElement):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.text}"


class Button (UIElement):
    def __init__(self, width, height, background_color,x, y, text):
        super().__init__(x ,y, text)
        self.width = width
        self.height = height
        self.background_color = background_color

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.text}, {self.width},{self.height},{self.background_color}."


label = Label(8, 5, "hi")
print(label)

button = Button(60, 90, "blue", 6, 9, "bye")
print(button)
