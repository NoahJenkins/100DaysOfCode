import tkinter

window = tkinter.Tk()
window.title('My 1st GUI Program')
window.minsize(width=500,height=300)

#Label
label = tkinter.Label(text="I am a label :)", font=("Arial", 24, "bold"))
label.pack(side="left")

#Advange Arguments in Python:
#You can create arguments with default values. 
import turtle

tim = turtle.Turtle()
tim.write('hello')




window.mainloop()
    