import turtle
flag = turtle.Turtle()
flag.speed(3)
flag.pensize(5)
flag.color('#270082')
def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()
    
for i in range(24):
    flag.forward(80)
    flag.backward(80)
    flag.left(15)   
draw(0,-80)
flag.circle(80,360)
 #green#
flag.color('green')
flag.begin_fill()
flag.forward(300)
flag.backward(600)
flag.right(90)
flag.forward(150)
flag.left(90)
flag.forward(600)
flag.left(90)
flag.forward(150)
flag.left(90)
flag.end_fill()
 #saffron#
flag.color('orange')
draw(-300,80)
flag.begin_fill()
flag.right(180)
flag.forward(600)
flag.left(90)
flag.forward(150)
flag.left(90)
flag.forward(600)
flag.left(90)
flag.forward(150)
flag.end_fill()


turtle.done()   