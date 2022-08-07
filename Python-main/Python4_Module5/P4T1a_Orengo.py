
# Import turtle
import turtle
win = turtle.Screen()
t = turtle.Turtle()

#Display options
t.pensize(3)
t.pencolor("black")
t.shape("turtle")
win.bgcolor

# Initiate loop for square
for i in range(4):
    t.forward(150)
    t.left(90)
t.goto(0,150)
# Initiate loop for triangle
for i in range(3):
    t.forward(150)
    t.left(120)
