import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("white")     # set pencolor (takes string)
t.shape("turtle")
win.bgcolor("blue")     # change the background color of window

# commands from here to the last line can be replaced

# initial setup
# create letter "A"
t.goto(20,70)
t.goto(40,0)
t.penup()
t.goto(10,35)
t.pendown()
t.goto(30,35)
t.penup()

# create letter "O" 
t.goto(80,0)
t.pendown()
t.circle(35)
t.penup()

# Goto coordinates and change color
t.goto(-10,-30)
t.pendown()
t.pensize(5)
t.pencolor("red")

# initiates loop to draw box
for i in range(4):
    t.forward(133)
    t.left(90)

# screen blinks    
for i in range(100):
    win.bgcolor("white")
    win.bgcolor("blue")

# end commands
win.exitonclick()

