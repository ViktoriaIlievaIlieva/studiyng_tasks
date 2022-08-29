

type_of = type(5)
# print(type_of)

#------------------------------------------------------------------------------------------------------------

class Circle:
    def __init__(self):
        self.radius = 5

my_circle = Circle()

my_circle_type = type(my_circle)
# print(my_circle_type)

# print(my_circle.radius)


#------------------------------------------------------------------------------------------------------------

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        circle_perimiter = 2 * self.radius * 3.14
        return circle_perimiter


my_circle = Circle(6)

print(my_circle.radius)

perimeter = my_circle.perimeter()
print(perimeter)

#------------------------------------------------------------------------------------------------------------

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

my_user = User("viki", "example")

print(my_user.username)
print(my_user.password)