from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("green")
        self.lastx = self.xcor()
        self.lasty = self.ycor()

    def ball_move(self):
        self.up()
        self.goto(self.xcor()+15,self.ycor()+15)
        self.down()

        # if self.ycor()==280 and self.xcor() > self.lastx or self.xcor() == -380 and  self.ycor() < self.lasty:
        #     self.rt(60)
        
        if self.ycor() > 280 or self.ycor() < -280:
            self.setx(180)