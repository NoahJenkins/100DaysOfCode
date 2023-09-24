from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.goto(STARTING_POSITION)
        self.player_forward()

    def player_forward(self):
        self.forward(MOVE_DISTANCE)


turtle = Player()

screen.onkey(turtle.player_forward, 'Up')
screen.exitonclick()



