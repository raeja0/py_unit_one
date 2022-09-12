# remember to use comments!
import turtle

turtle.speed(100)
def makealargesquare():
    for x in range(4):
        turtle.forward(200)
        turtle.left(90)

def makeamediumsquare():
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)

def makeasmallsquare():
    for x in range(4):
        turtle.forward(50)
        turtle.left(90)

for y in range (40):
    makealargesquare()
    turtle.left(3)
    makeamediumsquare()
    turtle.left(3)
    makeasmallsquare()
    turtle.left(3)

turtle.exitonclick()
