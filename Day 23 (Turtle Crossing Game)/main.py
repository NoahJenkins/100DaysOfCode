import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
cars = []
first_car = CarManager()
cars.append(first_car)
screen.onkey(player.player_forward, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_count += 1
    if loop_count == 6:
        new_car = CarManager()
        cars.append(new_car)
        loop_count = 0
    
    for car in cars:
        car.driving()
        if player.distance(car) < 20:
            game_is_on = False

print("Game Over")
    
    
