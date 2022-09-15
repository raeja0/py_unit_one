import turtle

turtle.speed(8)

def space_house():
    turtle.left(90)
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()

def draw_house(house_size, house_color, roof_color):
    turtle.fillcolor(house_color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(house_size)
        turtle.left(90)
    turtle.right(270)
    turtle.forward(house_size)
    turtle.right(90)
    turtle.end_fill()
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    for y in range(4):
        turtle.forward(house_size)
        turtle.left(120)
    turtle.end_fill()
    turtle.right(210)
    turtle.forward(house_size)
    #turtle.left(90)

turtle.penup()
turtle.forward(-300)
turtle.pendown()

for z in range(1):
    draw_house(150, 'red', 'blue')
    space_house()
    draw_house(50, 'green', 'purple')
    space_house()
    draw_house(100, 'light blue', 'pink')
    space_house()
    draw_house(200, 'purple', 'green')
turtle.exitonclick()