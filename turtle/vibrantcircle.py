from turtle import Turtle,Screen


cursor = Turtle()
screen = Screen()

a = 0
b = 0

cursor.pen(fillcolor="green",pensize=3,speed=0)
cursor.pencolor("green")
screen.bgcolor("black")

cursor.up()
cursor.goto(0,200)
cursor.down()

while True:
    cursor.fd(a)
    cursor.rt(b)
    a +=3
    b+=1
    if b == 210:
        break
    cursor.hideturtle()

screen.exitonclick()

