from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.hideturtle()
        self.color("white")
        self.up()
        self.goto(-50,270)
        self.down()
        self.write(f"Scoreboad : {self.count}",align="left", font=("Arial", 20, "normal"))
        
    def gameover(self):
        self.up()
        self.goto(0,0)
        self.down()
        self.write(f"Game over ",align="left", font=("Arial", 20, "normal"))

    def increase(self):
        self.count +=1
        self.clear()
        self.write(f"Scoreboad : {self.count}",align="left", font=("Arial", 20, "normal"))