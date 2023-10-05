from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.left(90)
        self.goto(STARTING_POSITION)
        self.player_forward()

    def player_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def player_reset(self):
        self.goto(STARTING_POSITION)






