import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("black")     # set pencolor (takes string)
t.shape("turtle")
win.bgcolor("white")

#Letter "A"
t.penup()
t.goto(-120,0)
t.pendown()
t.left(60)
t.forward(90)
t.right(120)
t.forward(90)
t.penup()
t.goto(-120,45)
t.pendown()
t.goto(-30,45)

#Letter "M"
t.penup()
t.goto(0,0)
t.pendown()
t.goto(35,70)
t.goto(50,35)
t.goto(65,70)
t.goto(100,0)

#Letter "O"
t.penup()
t.goto(130,15)
t.pendown()
t.circle(42)
