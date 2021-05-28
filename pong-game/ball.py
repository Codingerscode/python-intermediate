from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("green")
        self.x_move = 10
        self.y_move = 10
        self.seth(40)
        self.movespead = 0.1
        

    def ball_move(self):
        self.up()
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
        
    def bounce(self):
        self.y_move *= -1

    def collisionbounce(self):
        self.x_move *= -1
        self.movespead *=0.9

    
        