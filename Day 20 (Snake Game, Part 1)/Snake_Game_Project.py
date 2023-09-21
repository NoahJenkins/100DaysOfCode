from turtle import Turtle, Screen
import random
import time
from snake import Snake

#Screen Set Up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Noah's Snake Game")
screen.tracer(0)

snake = Snake()
snake.create_snake()

screen.listen()
screen.onkey(snake.up,'up')
screen.onkey(snake.down,'down')
screen.onkey(snake.left,'left')
screen.onkey(snake.right, 'right')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()


        


screen.exitonclick()
