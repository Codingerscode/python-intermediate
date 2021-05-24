from turtle import Turtle,Screen

cursor = Turtle()
screen = Screen()

def moveforward():
    cursor.fd(10)

screen.listen()
screen.onkey(key="space" , fun=moveforward)

screen.exitonclick()