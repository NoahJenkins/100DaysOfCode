import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

#Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#Scoreboard
scoreboard = Scoreboard()

# Create Player
player = Player()

cars = CarManager()
cars.create_car()

# Player control
screen.onkey(player.player_forward, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.driving()
    loop_count += 1
    if loop_count == 6:
        cars.create_car()
        loop_count = 0
    
    # Check if a line has been crossed
    if player.ycor() == FINISH_LINE_Y:
        player.player_reset()
        cars.level_up()
        scoreboard.point()

    #Car driving & checking if car has squished turtle
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    
    
scoreboard.game_over()
screen.exitonclick()
    
    
