import turtle

length = 5
speed = 20
for i in range(30):
    turtle.seth(0)
    turtle.forward(length)
    turtle.seth(90)
    turtle.forward(length)
    turtle.seth(180)
    length+=5
    turtle.forward(length)
    turtle.seth(270)
    turtle.forward(length)
    length+=5
turtle.done()