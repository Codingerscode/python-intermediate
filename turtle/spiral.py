import random
from turtle import Turtle,Screen

cursor = Turtle()
screen = Screen()

cursor.pen(fillcolor="black",pensize=1,speed=10000)
screen.colormode(255)
screen.bgcolor("black")

deg = int(input("Enter the degree of shift"))

for i in range(int(360/deg)):
    cursor.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cursor.circle(100)
    cursor.seth(i*deg)
    

screen.exitonclick()
