import turtle

t = turtle.Turtle()
t.color("green")
t.pensize(4)
t.fillcolor("blue")

t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(72)
t.end_fill()

turtle.done()
