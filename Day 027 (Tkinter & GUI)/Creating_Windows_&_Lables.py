from tkinter import *

window = Tk()
window.title('My 1st GUI Program')
window.minsize(width=500,height=300)

#Label
label =Label(text="I am a label :)", font=("Arial", 24, "bold"))

def label_reveal():
    label.pack(side="left")

#Advange Arguments in Python:
#You can create arguments with default values. 
# import turtle

# tim = turtle.Turtle()
# tim.write('hello')

#Button
def button_click():
    print('I got clicked')

button =Button(text="click me", command = label_reveal)
button.pack()

input = Entry(width=10)
input.pack()
input.get()

window.mainloop()
    