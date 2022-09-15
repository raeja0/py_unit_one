# remember to use comments!
import turtle

turtle.speed(100)

def pentagon():
    turtle.color('light blue')
    for x in range(5):
        turtle.forward(100)
        turtle.left(72)

def diamond():
    turtle.color('pink')
    for x in range(2):
        turtle.forward(100)
        turtle.left(125)
        turtle.forward(100)
        turtle.left(55)

turtle.penup()
turtle.forward(-100)
turtle.pendown()

for x in range(20):
    diamond()
    turtle.left(9)
    pentagon()
    turtle.left(9)

turtle.exitonclick()
