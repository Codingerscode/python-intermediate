from turtle import Turtle

class Computer(Turtle):
    def __init__(self,position):
        super().__init__(shape="square")
        self.up()
        self.seth(90)
        self.pen(fillcolor="white",pensize=3,pencolor="white")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(position)
    
    def curup(self):
        self.fd(20)
        

    def curdown(self):
        self.back(20)
    
    
