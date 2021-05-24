from turtle import Turtle,Screen
from random import choice

cursor = Turtle()
screen = Screen()

screen.colormode(255)
screen.title("Sketch app")
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

def up():
    cursor.pen(fillcolor="red",pensize=5,speed=10)
    cursor.color(choice(color_list))
    screen.bgcolor(choice(color_list))
    
screen.listen()
screen.onkey(key="w" , fun=lambda:cursor.fd(15))
screen.onkey(key="s" , fun=lambda:cursor.back(15))
screen.onkey(key="a" , fun=lambda:cursor.lt(10))
screen.onkey(key="d" , fun=lambda:cursor.rt(10))
screen.onkey(key="c" , fun=lambda:screen.reset())
screen.onkey(key="u" , fun=lambda:cursor.undo())
screen.onkey(key="p" , fun=lambda:cursor.up())
screen.onkey(key="o" , fun=lambda:cursor.down())
screen.onkey(key="x",fun=up)

screen.exitonclick()