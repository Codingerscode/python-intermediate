from turtle import Turtle,Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.snake = [Turtle(shape="circle") for _ in range(3)]
        self.screen.bgcolor("black")
        self.screen.setup(width=600,height=600)
        self.screen.title("Snake game")
        for i in range(3):
            self.snake[i].color("green")
            self.snake[i].up()
            self.snake[i].setpos(x=i*-20,y=0.0)
    
    def move(self):
        self.screen.tracer(0)
        while True:
            self.screen.update() 
            time.sleep(0.1)
            for i in range(len(self.snake)-1,0,-1):
                self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
            self.snake[0].fd(20)

    def left(self):
        self.screen.update()
        time.sleep(0.1)
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        if self.snake[0].heading()!=RIGHT:
            self.snake[0].seth(LEFT)
            self.snake[0].fd(20)

    def right(self):
        self.screen.update()
        time.sleep(0.1)
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        if self.snake[0].heading()!=LEFT:
            self.snake[0].seth(RIGHT)
            self.snake[0].fd(20)

    def down(self):
        self.screen.update()
        time.sleep(0.1)
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        if self.snake[0].heading()!=UP:
            self.snake[0].seth(DOWN)
            self.snake[0].fd(20)

    def up(self):
        self.screen.update()
        time.sleep(0.1)
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        if self.snake[0].heading()!=DOWN:
            self.snake[0].seth(UP)
            self.snake[0].fd(20)

