from turtle import Turtle
from turtle import Screen
import random
import turtle as t


tim = Turtle()
t.colormode(255)

def random_color():
 r = random.randint(0,255)
 g = random.randint(0,255)
 b = random.randint(0,255)
 color = (r, g, b)
 return color

tim.speed('fastest')

def draw_spirograph(size_of_graph):
   for num in range(int(360/size_of_graph)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)
    print(tim.heading)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

