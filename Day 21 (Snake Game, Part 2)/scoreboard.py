from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        score_text = f'Score: {self.score}'
        self.write(score_text, align="center", font=("Helvetica", 16, "normal",))
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown
        self.score = 0



#test code
# screen = Screen()
# screen.screensize(600,600)
# screen.bgcolor('black')
# test = Scoreboard()

# test.write_score()
# screen.exitonclick()
    


    