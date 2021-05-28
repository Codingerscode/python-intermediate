from turtle import Turtle,Screen
from random import randint

cursor = Turtle()
cursor.pen(fillcolor="black",pensize=3,pencolor='red',speed=1)
cursor.shapesize(3,2,1)
screen = Screen()
screen.colormode(255)


for i in range(3,10):
    screen.bgcolor(randint(0,255),randint(0,255),randint(0,255))
    cursor.color(randint(0,255),randint(0,255),randint(0,255))
    # cursor.begin_fill()
    for j in range(i):
        cursor.rt(360/i)
        cursor.fd(100+i)
    # cursor.end_fill()

screen.exitonclick()

