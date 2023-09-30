from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checks, reps
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    checks = ""
    checkmark.config(text=checks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 ==0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global checks, timer

    count_min = math.floor(count / 60)
    count_sec = round((count % 60),0)
    if count_sec < 10:
        count_sec=f"0{count}"

    canvas.itemconfig(time_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count -1)
    else: 
        start_timer()
        if reps % 2 == 0:
            checks += "✔"
            checkmark.config(text = checks)

# ---------------------------- UI SETUP ------------------------------- #
#Window Set Up
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas Set Up
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
time_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(row=1,column=1)

#Title Label
title = Label(text="Timer", font=(FONT_NAME,50, "normal" ), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)

#Start Button
start = Button(text="Start", highlightthickness=0, command= start_timer)
start.grid(row=2, column=0)

#Reset Button
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

# Checkmark Label
checkmark = Label(text=checks, bg=YELLOW,fg=GREEN)
checkmark.grid(row=3,column=1)

#Keep window running
window.mainloop()