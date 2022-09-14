import turtle

turtle.ht()

from turtle import *
color('red')
begin_fill()
while True:
    for x in range(4):
        turtle.forward(200)
        turtle.right(90)
    if abs(pos()) < 1:
        break
end_fill()

color('blue')
begin_fill()
while True:
    for y in range(3):
        turtle.forward(200)
        turtle.left(120)
    if abs(pos()) < 1:
        break
end_fill()
done()

turtle.exitonclick()