# WAP For the Create the the tutle basic function and all

import turtle

# Create screen
screen = turtle.Screen()
screen.title("Turtle Basics")
screen.bgcolor("lightblue")

# Create turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("darkgreen")
pen.pensize(3)
pen.speed(3)

# Functions
def move_forward():
    pen.forward(100)

def move_backward():
    pen.backward(100)

def turn_left():
    pen.left(45)

def turn_right():
    pen.right(45)

def pen_up():
    pen.penup()

def pen_down():
    pen.pendown()

def clear_screen():
    pen.clear()

def reset_turtle():
    pen.reset()

def exit_program():
    screen.bye()

# Keyboard Bindings
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "p")
screen.onkey(clear_screen, "c")
screen.onkey(reset_turtle, "r")
screen.onkey(exit_program, "q")

# Run turtle window
screen.mainloop()