from turtle import Turtle

class Computer(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.cursor = [Turtle(shape="square") for _ in range(3)]
        for i in range(len(self.cursor)):
            self.cursor[i].pen(fillcolor="white",pensize=3,speed=0,pencolor="white")
            self.cursor[i].up()
            self.cursor[i].goto(x=360,y=i*20)