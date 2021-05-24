from snake import Snake
from food import Food

import time


snake = Snake()
food = Food()

snake.screen.listen()
snake.screen.onkey(fun=snake.up,key="Up")
snake.screen.onkey(fun=snake.down,key="Down")
snake.screen.onkey(fun=snake.left,key="Left")
snake.screen.onkey(fun=snake.right,key="Right")

while True:
    snake.screen.update() 
    time.sleep(0.1)
    snake.move()

    #detect collision from food
    if snake.snake[0].distance() < 15:
        print("nyom nyom nyom")
    
    


    

snake.screen.exitonclick()