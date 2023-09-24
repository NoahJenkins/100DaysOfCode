from turtle import Turtle, Screen
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(x=280,y=random.randint(-250,280))
        new_car.left(180)
        self.all_cars.append(new_car)



    def driving(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


        

