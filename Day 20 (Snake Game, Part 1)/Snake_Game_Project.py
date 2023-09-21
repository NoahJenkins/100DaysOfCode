from turtle import Turtle, Screen
import random


#Snake body Set Up
starting_positions =[(0,0), (-20,0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto (position)


#Screen Set Up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Noah's Snake Game")
screen.exitonclick()
