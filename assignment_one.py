# remember to use comments!
import turtle # Opens turtle

turtle.speed(100) # Sets the speed to a fast pase

def pentagon(): # Defines how to make a pentagon
    turtle.color('light blue')
    for x in range(5):
        turtle.forward(75)
        turtle.left(72)

def diamond(): # Defines how to make a diamond
    turtle.color('pink')
    for x in range(2):
        turtle.forward(75)
        turtle.left(125)
        turtle.forward(75)
        turtle.left(55)

def square(): # Defines how to make a square
    turtle.color('blue')
    for x in range(4):
        turtle.forward(75)
        turtle.left(90)

def decahedron(): # Defines how to make a decahedron
    turtle.color('red')
    for x in range(10):
        turtle.forward(45)
        turtle.left(36)

turtle.penup() # Sets turtle starting location
turtle.forward(-200)
turtle.pendown()
# Draws first mosaic
for x in range(20):
    diamond()
    turtle.left(9)
    pentagon()
    turtle.left(9)

turtle.penup() # Sets location for the second mosaic
turtle.goto(200, 0)
turtle.pendown()

for x in range(20): # Draws second mosaic
    decahedron()
    turtle.left(9)
    square()
    turtle.left(9)

turtle.exitonclick() # Closes turtle when clicked outside of screen
