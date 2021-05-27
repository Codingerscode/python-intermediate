from turtle import Turtle , Screen 
import time
from ball import Ball
from computer import Computer
from score import Score


#setting up screen
screen = Screen()
screen.setup(width=800,height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")

#making of player
cursor = [Turtle(shape="square") for _ in range(3)]
for i in range(len(cursor)):
    cursor[i].pen(fillcolor="white",pensize=3,speed=0,pencolor="white")
    cursor[i].up()
    cursor[i].goto(x=-370,y=i*20)


#creation of computer 
comp = Computer()

#creation of score
score = Score()

#creation of ball
ball = Ball()


def userup():
    pass


def userdown():
    pass

#event listener
screen.listen()
screen.onkey(key="Up",fun=userup())
screen.onkey(key="Down",fun=userdown())


#game loop
running  = True
while running:
    score.computer_score()
    score.user_score()

    ball.ball_move()


screen.exitonclick()

