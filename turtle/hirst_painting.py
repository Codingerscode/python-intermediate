from turtle import Turtle,Screen
from colorgram import extract
from random import choice

cursor = Turtle()
cursor.shape("circle")
cursor.pen(fillcolor="red",pensize=5,pencolor="black")
cursor.up()
cursor.goto(-270,-270)
cursor.down()

screen = Screen()
screen.title("Welcome to 2.2 billion painting")
screen.colormode(255)
screen.setup(width=600,height=600)


colors = extract("imagess.jpg",35)
list_colors = []
for i in range(35):
    list_colors.append(tuple(colors[i].rgb))


def jump():
    cursor.up()
    cursor.fd(40)
    cursor.down()

def turnleft():
    cursor.lt(90)
    jump()
    cursor.lt(90)
    cursor.up()
    cursor.fd(40)
    cursor.down()
    

def turnright():
    cursor.rt(90)
    jump()
    cursor.rt(90)
    cursor.up()
    cursor.fd(40)
    cursor.down()

main_x = cursor.xcor()
flag = 0

num = int(screen.numinput(title="dots in painting",prompt="How many dots you want in painting"))



for i in range(num):
    if cursor.xcor() >= 270.0:
        flag = 1
        turnleft()
        
    elif cursor.xcor() < -270.0 and flag == 1:
        turnright()
        flag = 0
    
    else:
        cursor.dot(20,choice(list_colors))
        jump()

cursor.hideturtle()
screen.exitonclick()

