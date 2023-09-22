from turtle import Turtle, Screen
import random

#Food class is inheriting all methods and attributes from turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        random_x =random.randint(-280,280)
        random_y =random.randint(-280,280)
        self.goto(random_x, random_y)

food = Food()
screen = Screen()
screen.exitonclick()


        