from turtle import Turtle, Screen
import random
import time
from snake import Snake
from Food import Food

#Screen Set Up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Noah's Snake Game")
screen.tracer(0)

#Setting up Snake object from class.
snake = Snake()
snake.create_snake()

#Setting up Food Object from Food Class:
food = Food()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right, 'Right')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()


        

