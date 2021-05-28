from turtle import Turtle
from ball import Ball

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.com = 0
        self.user = 0

    def computer_score(self):
        self.hideturtle()
        self.up()
        self.goto(x = -50 , y = 270)
        self.down()
        self.color("white")
        self.write(f"{self.com}",align="left", font=("Arial", 20, "normal"))

    def user_score(self):
        self.hideturtle()
        self.up()
        self.goto(x = 50 , y = 270)
        self.down()
        self.color("white")
        self.write(f"{self.user}",align="left", font=("Arial", 20, "normal"))

    def win(self):
        self.hideturtle()
        self.up()
        self.goto(x = -50 , y = 270)
        self.down()
        self.color("black")
        self.write(f"game over",align="left", font=("Arial", 20, "normal"))