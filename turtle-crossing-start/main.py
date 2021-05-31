import turtle
import time
# from playsound import playsound
# from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=450)
screen.bgpic("road.gif")
screen.register_shape('car3.gif')
screen.register_shape('car4.gif')
# screen.register_shape('bus.gif')
screen.tracer(0)


# playsound('background.wav')
player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up",fun=lambda:player.fd(8))
screen.onkeypress(key="Down",fun=lambda:player.bk(8))



score.showscore()
count = 0
game_is_on = True
while game_is_on:
    if count%5 == 0:
        cars.createcar()

    cars.move()
    time.sleep(score.level)
    screen.update()

    if player.ycor() >195:
        score.level +=1
        

    count += 1

screen.exitonclick()