from tkinter import *
import customtkinter as ct
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60
reps = 0
timer = None
# --------------timer reset-----------------

def reset_timer():
    window.after_cancel(timer)
    count_timer.configure(count_timer, text="00:00")
    timer_label.configure(text="Timer", text_color="green")
    check_label.configure(text="")
    global reps
    reps = 0
# --------------timer mechanism------------

def start_timer():
    global reps
    reps += 1

    work = WORK_MIN 
    rest = SHORT_BREAK  
    big_break = LONG_BREAK  

    if reps % 8 == 0:
        count_down(big_break)
        timer_label.configure(text='Break', text_color=RED)
    elif reps % 2 == 0:
        count_down(rest)
        timer_label.configure(text="Rest", text_color=PINK)
    else:
        count_down(work)
        timer_label.configure(text="Work", text_color=GREEN)

# -------------countdown-------------------

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    count_timer.configure(count_timer, text=(f"{minutes}:{seconds}"))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            check_label.configure(text=mark)


# -------------------UI--------------------
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

window = ct.CTk()
window.geometry("320x300")
window.configure(pady=20, padx=20)

timer_label = ct.CTkLabel(text="Timer",
                          text_color="green",
                          text_font=("Ariel", 30),
                          pady=15)

timer_label.grid(row=0, column=0, columnspan=2)


count_timer = ct.CTkLabel(text="00:00",
                    text_font=("Ariel", 30, "bold"))
count_timer.grid(row=1, column=0, columnspan=2)



start = ct.CTkButton(text="Start", command=start_timer)
window.config(padx=10)
start.grid(row=2, column=0)

stop = ct.CTkButton(text="Stop", command=reset_timer)
stop.grid(row=2, column=1)
stop.config(padx=10)

check_label = ct.CTkLabel(text='', text_color=GREEN)
check_label.grid(row=4, column=0, columnspan=2)


window.mainloop()
