from turtle import Turtle 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("white")
        self.up()
        self.seth(90)
        self.goto(x=0.0,y=-200)
        
        
