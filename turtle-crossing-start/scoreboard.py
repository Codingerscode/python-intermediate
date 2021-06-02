from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open("data.txt") as data:
            self.highlevel = int(data.read())
        self.ht()
        self.up()
        self.goto(x=-270,y=190)

    def showscore(self):
        self.clear()
        self.write(f"Level: {self.level} High score: {self.highlevel}",align="left", font=FONT)

    def goodbye(self):
        self.goto(-70,0)
        self.color("white")
        self.write("Game over",align="left", font=FONT)

