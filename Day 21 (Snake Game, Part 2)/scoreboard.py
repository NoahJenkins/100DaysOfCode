from turtle import Turtle, Screen

#Constants
ALIGHMENT = 'center'
FONT = ("Helvetica", 16, "normal",)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown
        self.score = 0
        score_text = f'Score: {self.score}'
        self.write(score_text, align=ALIGHMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        score_text = f'Score: {self.score}'
        self.write(score_text, align=ALIGHMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown
        self.write('GAME OVER', align=ALIGHMENT, font=FONT)




#test code
# screen = Screen()
# screen.screensize(600,600)
# screen.bgcolor('black')
# test = Scoreboard()

# test.write_score()
# screen.exitonclick()
    


    