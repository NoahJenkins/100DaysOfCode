from turtle import Turtle
from turtle import Screen
import random


# challange 4:

tim = Turtle()
tim.speed('fastest')
tim.pensize(10)
colors = ['red', "orange", 'green', 'blue', 'pink']
directions = [0, 90, 180, 270]

for num in range(200):
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = Screen()
screen.exitonclick()
