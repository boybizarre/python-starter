from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_mark.config(text='')
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # if it's the 8th rep:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        # if it's the 2nd/ 4th/ 6th rep:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        # if it's the 1st /3rd / 5th / 7th rep:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)


def count_down(count):
    # print(count)

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}: {seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
      start_timer()
      marks = ''
      work_sessions = math.floor(reps / 2)
      for _ in range(work_sessions):
          marks += '✓'
          check_mark.config(text=marks)

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage 
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start_button = Button(text='Start', command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2,)

reset_button = Button(text='Reset', command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2,)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)





window.mainloop()
