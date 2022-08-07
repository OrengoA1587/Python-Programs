import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(5)
t.speed(1000)   # increase pensize (takes integer)
t.pencolor("white")     # set pencolor (takes string)
t.shape("turtle")
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


    


 

    

    

