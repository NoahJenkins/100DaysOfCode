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
 return (r, g, b)

tim.speed('fastest')
tim.pensize(10)
directions = [0, 90, 180, 270]

for num in range(200):
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = Screen()
screen.exitonclick()

#A tuple is made with a (), rather than []
my_tuple = (1,3,8)
my_tuple[2]

#A Tuple is carved in stone, its values cannot be changes, unlike a list
#You cannot re-assign values, append or remove, it is immutable. 
