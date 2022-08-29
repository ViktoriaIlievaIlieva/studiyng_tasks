from turtle import *
color("pink")
bgcolor("black")
speed(11)
hideturtle()
b = 0

penup()
left(90)
forward(150)
pendown()
right(90)

while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1