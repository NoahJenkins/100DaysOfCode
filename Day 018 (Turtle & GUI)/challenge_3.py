from turtle import Turtle
from turtle import Screen
import random


# Challenge 3:

tim = Turtle()

# def triangle():
#     for num in range(3):
#         timmy.color("red")
#         timmy.forward(30)
#         timmy.right(120)

# def square():
#     for num in range(4):
#         timmy.color("green")
#         timmy.forward(40)
#         timmy.right(90)

# def pentagon():
#     for num in range(5):
#         timmy.color("blue")
#         timmy.forward(50)
#         timmy.right(72)

# def hexagon():
#     for num in range(6):
#         timmy.color("purple")
#         timmy.forward(60)
#         timmy.right(60)

# triangle()
# square()
# pentagon()
# hexagon()

colors = ['red', "orange", 'green', 'blue', 'pink']

def draw_shape(num_sides):
    for num in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()