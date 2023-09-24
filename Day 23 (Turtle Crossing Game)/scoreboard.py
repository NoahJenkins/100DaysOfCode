FONT = ("Courier", 24, "normal")


from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.score = 1
        self.write(f'Level: {self.score}', align="left", font=FONT)
        
    def update_score(self):
        self.write(f'Level: {self.score}', align="left", font=FONT)


    def point(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over!', align="center", font=FONT)

