import turtle

turtle.setup(650,350,None,None)
turtle.penup()#抬起画笔
turtle.fd(-250)#不绘制
turtle.pendown()#落下画笔，开始绘制
turtle.pencolor("yellow")
turtle.pensize(25)
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()