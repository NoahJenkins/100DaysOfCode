from turtle import Turtle, Screen
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('normal')
        self.penup()
        self.color('white')
        self.shape('square')
    
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
    
    def bounce(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() -10
        self.goto(new_x, new_y)


#Test Code
screen=Screen()
screen.setup(width=800, height= 600)

ball = Ball()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor > 300 or ball.ycor < -300:
        ball.bounce()
screen.exitonclick()
