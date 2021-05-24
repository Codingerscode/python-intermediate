from random import randint,choice
from turtle import Turtle,Screen

cursor = Turtle()
screen = Screen()

cursor.pen(fillcolor="black",pensize=8,speed=10,pencolor="red")
cursor.shapesize(3,2,1)
screen.colormode(255)

angles = [90,180,270,360]
i = 0

for _ in range(700):
    cursor.color(randint(0,255),randint(0,255),randint(0,255))
    cursor.fd(20)
    cursor.seth(choice(angles))
    


screen.exitonclick()