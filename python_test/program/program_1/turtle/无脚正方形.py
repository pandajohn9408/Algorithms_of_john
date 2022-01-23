import turtle

turtle.setup(400,400,100,100)
for i in range(4):
    turtle.seth(i*90)
    turtle.penup()
    turtle.fd(20)
    turtle.down()
    turtle.fd(260)
    turtle.penup()
    turtle.fd(20)
    turtle.down()
turtle.done()