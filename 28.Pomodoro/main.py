#!/usr/bin/env python
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    #Deffining the routime of Pomodoro system
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(int(LONG_BREAK_MIN*60))
        label.config(text="Long Break", fg = RED)
    elif reps % 2 == 0:
        count_down(int(SHORT_BREAK_MIN*60))
        label.config(text="Break", fg = PINK)
    else:
        count_down(int(WORK_MIN*60))
        label.config(text="Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = count//60
    seconds = count%60

    #formatting the output seconds and minutes
    if seconds<10:
        seconds=f"0{seconds}"
    if minutes<10:
        minutes=f"0{minutes}"

    format_count = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text,text=format_count)
    if count > 0:
        timer = window.after(1000, *(count_down,count-1))
    else:
        start_timer()
        mark = ""
        for _ in range(int(reps/2)):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro System")
window.config(padx=100,pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,132,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

label = Label(window,text="Timer",
              foreground=GREEN,
              bg=YELLOW,
              font=(FONT_NAME,35,"bold"))

label.grid(row=0,column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)
reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(row=2,column=3)

check_label = Label(window,text="",
                    foreground=GREEN,
                    bg=YELLOW,
                    font=(FONT_NAME,15,"bold"))
check_label.grid(row=3,column=1)




window.mainloop()