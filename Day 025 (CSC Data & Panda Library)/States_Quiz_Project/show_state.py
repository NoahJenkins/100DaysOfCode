from turtle import Turtle, Screen
FONT = ("Courier", 12, "normal")


class show_answer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def write_answer(self, x,y, state):
        self.goto(x,y)
        self.write(f'{state}', align="center", font=FONT)