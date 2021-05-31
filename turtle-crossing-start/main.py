import turtle
import time
# from playsound import playsound
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#setting up screen
screen = turtle.Screen()
screen.setup(width=600, height=450)
screen.bgpic("road.gif")
screen.register_shape('car3.gif')
screen.register_shape('car4.gif')
screen.tracer(0)


#setting up object
# playsound('background.wav')
player = Player()
cars = CarManager()
score = Scoreboard()


#setting up event - listener
screen.listen()
screen.onkeypress(key="Up",fun=lambda:player.fd(10))
screen.onkeypress(key="Down",fun=lambda:player.bk(10))


#showing up score   
score.showscore()
count = 0
game_is_on = True
while game_is_on:
    if count%5 == 0:
        cars.createcar()

    cars.move()
    time.sleep( 0.1 / (2 * score.level))
    screen.update()

#increament of score
    if player.ycor() >195:
        score.level +=1
        score.showscore()
        player.up()
        player.seth(90)
        player.goto(x=0.0,y=-200)

#checking of collision   
    for i  in cars.cars:
        if i.distance(player) < 20:
            game_is_on = False

    count += 1


# screen.clearscreen()
score.goodbye()
screen.exitonclick()