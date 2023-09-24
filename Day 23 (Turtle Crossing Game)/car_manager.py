from turtle import Turtle, Screen
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(x=280,y=random.randint(-280,280))
        self.left(180)


    def driving(self):
        self.forward(STARTING_MOVE_DISTANCE)

        

