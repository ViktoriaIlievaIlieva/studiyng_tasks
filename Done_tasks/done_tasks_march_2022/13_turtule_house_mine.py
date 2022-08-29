# Използвай tutle, за да нарисуваш символ на къщичка

import turtle

# turtle shape и функции
turtle.shape("turtle")
turtle.speed(0)


# трева
turtle.fillcolor("green")
turtle.begin_fill()
turtle.back(300)
turtle.forward(600)
turtle.seth(90)
turtle.forward(10)
turtle.seth(180)
turtle.forward(600)
turtle.seth(90)
turtle.right(180)
turtle.forward(10)
turtle.end_fill()

# стартова точка за къща
turtle.right(180)
turtle.forward(10)
turtle.seth(0)
turtle.forward(300)

# основа къща
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.seth(90)
turtle.forward(100)

turtle.seth(180)
turtle.forward(100)

turtle.seth(270)
turtle.forward(100)
turtle.end_fill()

# стартова точка за покрив
turtle.seth(90)
turtle.forward(100)

print(turtle.pos()) # (-100.00,110.00)

# покрив
turtle.fillcolor("purple")
turtle.begin_fill()
turtle.right(30)
turtle.forward(100)

turtle.right(120)
turtle.forward(100)
turtle.end_fill()

# стартова позиция комин
turtle.right(180)
turtle.forward(50)

# комин
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.right(80)
turtle.forward(20)
turtle.left(90)
turtle.forward(12)
turtle.left(90)
turtle.forward(20)
turtle.end_fill()

# стартова позиция комин
turtle.right(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(6)
turtle.left(90)

# дим
turtle.up()
turtle.left(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.right(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.right(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.left(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.left(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.left(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.right(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.right(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.left(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

turtle.up()
turtle.left(60)
turtle.forward(15)
turtle.down()
turtle.dot(5, "black")

# стартова точка прозорци
turtle.up()
turtle.goto(-100.00, 110.00)
turtle.seth(270)
turtle.forward(20)
turtle.seth(0)
turtle.forward(20)
# започване рисуване ляв прозорец


def window():
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.down()
    turtle.forward(20)
    turtle.seth(270)
    turtle.forward(20)
    turtle.seth(180)
    turtle.forward(20)
    turtle.seth(90)
    turtle.forward(20)
    turtle.seth(0)
    turtle.forward(10)
    turtle.seth(270)
    turtle.forward(20)
    turtle.seth(0)
    turtle.forward(10)
    turtle.seth(90)
    turtle.forward(10)
    turtle.seth(180)
    turtle.forward(20)
    turtle.seth(90)
    turtle.forward(10)
    turtle.seth(0)
    turtle.forward(20)
    turtle.seth(270)
    turtle.forward(20)
    turtle.seth(180)
    turtle.forward(20)
    turtle.seth(90)
    turtle.forward(20)
    turtle.end_fill()


window()

# позиция втори прозорец
turtle.up()
turtle.seth(0)
turtle.forward(40)
window()

# позиция врата
turtle.up()
turtle.seth(270)
turtle.forward(80)

# врата
turtle.fillcolor("white")
turtle.begin_fill()
turtle.down()
turtle.seth(90)
turtle.forward(40)
turtle.seth(180)
turtle.forward(20)
turtle.seth(270)
turtle.forward(40)
turtle.end_fill()


# позиция дръжка и дръжка
turtle.up()
turtle.seth(90)
turtle.forward(20)
turtle.seth(0)
turtle.forward(4)
turtle.down()
turtle.dot(5, "black")


# позиция първо цвете
turtle.up()
turtle.goto(-250.00, 10.00)
turtle.down()

# цвете


def leaf(side: int):
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(180 * side)
    turtle.left(30 * side)
    turtle.forward(10)
    turtle.left(30 * side)
    turtle.forward(10)

    turtle.left(135 * side)
    turtle.forward(10)
    turtle.left(60 * side)
    turtle.forward(10)
    turtle.end_fill()


def flower():
    # стъбло
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.seth(90)
    turtle.forward(20)
    turtle.seth(0)
    turtle.forward(3)
    turtle.seth(270)
    turtle.forward(20)
    turtle.end_fill()

    # ляво листо
    leaf(1)
    turtle.seth(270)
    # дясно листо
    leaf(-1)
    turtle.seth(90)

    # цвете част
    turtle.up()
    turtle.forward(30)
    turtle.down()
    turtle.dot(10, "yellow")

    turtle.up()
    turtle.seth(0)
    turtle.forward(10)
    turtle.down()
    turtle.dot(10, "blue")
    turtle.up()
    turtle.back(10)

    for _ in range(0, 8):
        turtle.up()
        turtle.left(45)
        turtle.forward(10)
        turtle.down()
        turtle.dot(10, "blue")
        turtle.up()
        turtle.back(10)


flower()

turtle.up()
turtle.goto(-150.00, 10.00)
turtle.down()

flower()

turtle.up()
turtle.goto(50.00, 10.00)
turtle.down()

flower()

turtle.up()
turtle.goto(150.00, 10.00)
turtle.down()

flower()

turtle.up()
turtle.goto(250.00, 10.00)
turtle.down()

flower()

turtle.up()
turtle.goto(250.00, 200.00)
turtle.down()


def cloud():
    turtle.dot(30, "blue")
    turtle.up()
    turtle.seth(180)
    turtle.right(45)
    turtle.forward(20)
    turtle.down()
    turtle.dot(35, "blue")

    turtle.up()
    turtle.seth(270)
    turtle.forward(25)
    turtle.down()
    turtle.dot(35, "blue")

    turtle.up()
    turtle.seth(180)
    turtle.right(45)
    turtle.forward(30)
    turtle.down()
    turtle.dot(45, "blue")

    turtle.up()
    turtle.seth(180)
    turtle.forward(10)
    turtle.seth(270)
    turtle.forward(15)
    turtle.down()
    turtle.dot(45, "blue")

cloud()

turtle.up()
turtle.goto(100.00, 150.00)
turtle.down()

cloud()

turtle.up()
turtle.goto(-150.00, 200.00)
turtle.down()

cloud()

# sun

turtle.up()
turtle.goto(-330.00, 220.00)
turtle.down()
turtle.dot(70, "yellow")

turtle.pensize(5)
turtle.pencolor("yellow")

turtle.up()
turtle.seth(0)
turtle.forward(40)
turtle.down()
turtle.forward(45)

for _ in range(0, 15):
    turtle.up()
    turtle.back(95)
    turtle.left(30)
    turtle.forward(40)
    turtle.down()
    turtle.forward(45)


turtle.hideturtle()

