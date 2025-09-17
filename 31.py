# Make the turtle code and create the pantagon and hexagon using python 

import turtle 

screen = turtle.Screen()
screen.bgcolor("Yellow")
screen.title("Pentagon and Hexagon With turtle")

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(5)

def draw_polygon(sides,length,color):
    pen.color(color)
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.left(angle)
# Drawing the pantagon

    pen.penup()
    pen.goto(-100,0)
    pen.pendown()
    pen.polygon(5,100,"Blue")

#Drawing Hexagon
pen.penup()
pen.goto(150, 0)  # Move turtle to right
pen.pendown()
draw_polygon(6, 100, "green")

pen.hideturtle()

screen.mainloop()