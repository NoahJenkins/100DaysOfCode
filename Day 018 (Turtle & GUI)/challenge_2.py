from turtle import Turtle
from turtle import Screen
# import random


# Challenge 2:
timmy = Turtle()
dash = 15
skip = 5

for num in range(20):
    timmy.pendown()
    timmy.forward(dash)
    timmy.penup()
    timmy.forward(skip)

screen = Screen()
screen.exitonclick()