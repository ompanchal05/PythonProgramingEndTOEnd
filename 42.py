# Create Pentagone using pen and turtle mode 

import turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.color("cyan")
pen.pensize(3)
pen.speed(5)

for _ in range(5):
    pen.forward(100)
    pen.left(72)

screen.exitonclick()