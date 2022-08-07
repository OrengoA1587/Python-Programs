import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(5)
t.speed(10000000)   # increase pensize (takes integer)
t.pencolor("white")     # set pencolor (takes string)
t.shape("triangle")
win.bgcolor("blue")

def branch():
    for i in range(4):
        t.forward(10)
        t.right(45)
        t.forward(25)
        t.backward(25)
        t.left(90)
        t.forward(25)
        t.backward(25)
        t.right(45)

def flake():
    for i in range(4):
        t.forward(15)
        t.left(90)

def mainFlake():
    for i in range(8):
        t.forward(45)
        t.right(60)
        branch()
        t.forward(10)
        t.right(45)
        flake()
        t.left(45)
        t.backward(50)
        t.left(105)    
t.color("black", "white")
t.begin_fill()

mainFlake()
t.penup()
t.goto(-240,120)
t.pendown()
mainFlake()
t.penup()
t.goto(-360,0)
t.pendown()
mainFlake()

t.end_fill()

##     for i in range(8):
##        t.forward(45)
##        t.right(60)
##        branch()
##        t.forward(10)
##        t.right(45)
##        flake()
##        t.left(45)
##        t.backward(50)
##        t.left(105)


 

    

    

