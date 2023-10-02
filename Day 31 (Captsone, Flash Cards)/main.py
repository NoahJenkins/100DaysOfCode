from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

###################  Catching FileNotFound Error ##################

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

######################  Create Flash Card #####################


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title, text= ("French"), fill = "black")
    canvas.itemconfig(card_text, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_background,image = card_front_img )
    flip_timer = window.after(3000, func=flip_card)


######################  Flip  Flash Card #####################

def flip_card():
    global current_card
    canvas.itemconfig(card_title,text="English", fill = "white")
    canvas.itemconfig(card_text,text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = card_back_image)

######################  Is Known Function #####################

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

###################### UI Set Up ##############################
#Window Set Up
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Canvas/Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file = "images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150,text="", font = ("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text = "", font = ("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Button Set Up. 
wrong_logo = PhotoImage(file = 'images/wrong.png')
wrong_but = Button(image=wrong_logo, highlightthickness=0)
wrong_but.grid(row = 1, column=0)

right_logo = PhotoImage(file = 'images/right.png')
right_but = Button(image=right_logo, highlightthickness=0, command=is_known)
right_but.grid(row = 1, column=1)



next_card()


window.mainloop()


