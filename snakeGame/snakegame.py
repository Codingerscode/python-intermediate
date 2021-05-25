from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Turtle

import time


snake = Snake()
food = Food()
score = Scoreboard()

flag = 1
snake.screen.listen()
snake.screen.onkey(fun=snake.up,key="Up")
snake.screen.onkey(fun=snake.down,key="Down")
snake.screen.onkey(fun=snake.left,key="Left")
snake.screen.onkey(fun=snake.right,key="Right")

while flag:
     
    snake.screen.update() 
    time.sleep(0.01)
    snake.move()

    #detect collision from food
    if snake.header.distance(food) <20:
        food.refresh()
        snake.snake.append(Turtle(shape="circle"))
        snake.snake[len(snake.snake)-1].up()
        snake.snake[len(snake.snake)-1].color("green")
        score.increase()

    if snake.header.xcor() > 280 or snake.header.xcor() < -280 or snake.header.ycor() > 280 or snake.header.ycor() < -280:
        score.gameover()
        break
    
    for i in range(1,len(snake.snake)):
        if snake.header.distance(snake.snake[i])<10:
            flag = 0
            score.gameover()
    


    

snake.screen.exitonclick()