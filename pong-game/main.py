from turtle import Turtle , Screen
import time
from random import choice
from ball import Ball
from computer import Computer
from score import Score


#setting up screen
screen = Screen()
screen.setup(width=800,height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)


#making of players
comp = Computer((350,0))
cursor = Computer((-350,0))
screen.update()

#creation of score
score = Score()

#creation of ball
ball = Ball()



#event listener
screen.listen()
screen.onkeypress(key="Up",fun=cursor.curup)
screen.onkeypress(key="Down",fun=cursor.curdown)
screen.onkeypress(key="w",fun=comp.curup)
screen.onkeypress(key="s",fun=comp.curdown)

#game loop
running  = True
while running:
    time.sleep(ball.movespead)

    screen.update()
    score.computer_score()
    score.user_score()
    ball.st()
    ball.ball_move()
    
    

    if ball.ycor() > 280 or ball.ycor()  < -280:
        ball.bounce()

    if ball.xcor() > 400:
        score.clear()
        score.user += 1
        ball.movespead = 0.1
        ball.ht()
        ball.up()
        ball.goto(0,0)
        ball.seth(choice([320,220,120,60]))
        ball.down()
        
    if ball.xcor() < -400:
        score.clear()
        score.com +=1
        ball.ht()
        ball.movespead = 0.1
        ball.up()
        ball.goto(0,0)
        ball.seth(choice([320,220,120,60]))
        ball.down()


    if cursor.distance(ball) < 20 or comp.distance(ball) < 20:
        ball.collisionbounce()
        
    
    if ball.distance(comp) < 50 and ball.xcor() > 320 or ball.distance(cursor) < 50 and ball.xcor() < -320 :
        ball.collisionbounce()
        
    
    if score.com == 10 or score.user == 10:
        break


screen.clearscreen()
score.win()
screen.exitonclick()

