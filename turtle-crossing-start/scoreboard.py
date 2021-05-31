from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.up()
        self.goto(x=-270,y=190)

    def showscore(self):
        self.write(f"Level: {self.level}",align="left", font=FONT)
        
