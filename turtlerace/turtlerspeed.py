from turtle import Turtle,Screen
from random import randint,choice

cursor = [Turtle(shape="turtle") for _ in range(6)]
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=600,height=600)
screen.bgcolor("black")

increase = 20
flag = True

color = screen.textinput(title="Color Color which color you want " ,prompt="which color you will bet on  \n red \n orange \n yellow \n green \n blue \n purple ")
color_list =iter(["red","orange","yellow","green","blue","purple"])


for i in cursor:
    i.color(next(color_list))
    i.up()
    i.goto(x = -270 , y =-270 + increase)
    i.down()
    increase +=90


while flag:
    for tur in cursor:
        tur.fd(randint(1,10))
        if tur.xcor() >250:
            flag = False
            screen.clearscreen()
            tur.write(f"I won ",align="left", font=("Arial", 70, "normal"))
            print(f"you won the bet" if tur.pencolor() == color else f"You lost the bet , {tur.pencolor()} won the race")

screen.exitonclick()
