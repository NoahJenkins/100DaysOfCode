from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        #Window
        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #Canvas/Question
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text=f'dummy text', font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        #Score Label
        self.score = Label(text=f'score: {0}', bg=THEME_COLOR, foreground="white")
        self.score.grid(row=0, column=1)
    
        #Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()

ui_test = QuizInterface()

