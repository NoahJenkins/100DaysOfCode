from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

#Crearion of sceeen object from screen class. 
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

#Creation of paddle object from paddle calss
r_paddle = Paddle(x_pos=350,y_pos= 0)
l_paddle = Paddle(x_pos=-350, y_pos=0)

#Creation of nall Object from Ball class
ball = Ball()

screen.listen()
#Right Player/Paddle Controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#Left Player/Paddle Controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Collission with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collission with r_paddle
    if  ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print('made contact')
        ball.bounce_x()








screen.exitonclick()