from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"




###################### UI Set Up ##############################
#Window Set Up
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas/Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image = card_front_img)
canvas.create_text(400, 150,text="Title", font = ("Arial", 40, "italic"))
canvas.create_text(400, 263, text = "word", font = ("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Button Set Up. 
wrong_logo = PhotoImage(file = 'images/wrong.png')
wrong_but = Button(image=wrong_logo, highlightthickness=0)
wrong_but.grid(row = 1, column=0)

right_logo = PhotoImage(file = 'images/right.png')
right_but = Button(image=right_logo, highlightthickness=0)
right_but.grid(row = 1, column=1)














window.mainloop()


