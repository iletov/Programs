import math
from tkinter import *
import customtkinter

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(count_timer, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    working = WORK_MIN * 60
    rest = SHORT_BREAK_MIN * 60
    big_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(big_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(rest)
        timer_label.config(text="Rest", fg=PINK)
    else:
        count_down(working)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(count_timer, text=(f"{minutes}:{seconds}"))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            check_label.config(text=mark)

        # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
space_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=space_img)
count_timer = canvas.create_text(100, 140, text="00:00", fill="#9C254D", font=("Ariel", 30, "bold"))
canvas.grid(row=2, column=1)


start = customtkinter.CTkButton(text="Start",bg=YELLOW, font=20, command=start_timer)
start.grid(row=3, column=0)

reset = customtkinter.CTkButton(text="Reset", bg=YELLOW, font=20, command=reset_timer)
reset.grid(row=3, column=2)

timer_label = customtkinter.CTkLabel(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, "bold"))
timer_label.grid(row=1, column=1)

check_label = customtkinter.CTkLabel(fg=GREEN, font=("Ariel", 20, "bold"))
check_label.grid(row=4, column=1)

window.mainloop()

