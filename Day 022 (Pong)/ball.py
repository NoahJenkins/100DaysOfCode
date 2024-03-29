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
        self.x_move=10
        self.y_move = 10
        self.current_speed = 0.1
    
    def move(self):
        '''Move logic for the ball to move'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        """Inverses the valye of y_move, which reverses the y velicity of the ball"""
        self.y_move *= -1

    def bounce_x(self):
        """Inverses the valye of y_move, which reverses the y velicity of the ball"""
        self.x_move *=-1
        self.current_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.current_speed = 0.1

# #Test Code
# screen=Screen()
# screen.setup(width=800, height= 600)
# screen.bgcolor('black')

# ball = Ball()
# game_is_on = True

# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()

#     if ball.ycor() > 300 or ball.ycor() < -300:
#         ball.bounce()

# screen.exitonclick()
