from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_pos,y=y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

