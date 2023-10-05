from turtle import Turtle
from turtle import Screen
import random
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')


# Challenge 1, make a square with the turtle.

def square_component():
    timmy.forward(100)
    timmy.right(90)
def make_square():
    square_component()
    square_component()
    square_component()  
    square_component()

make_square()

for num in range(4):
    timmy.forward(100)
    timmy.right(90)

# The exit screen on click has to happen last, so it is at the bottom of the file
screen = Screen()
screen.exitonclick()