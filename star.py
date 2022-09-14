import turtle

turtle.speed(1000)

from turtle import *
color('light blue', 'pink')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

turtle.exitonclick