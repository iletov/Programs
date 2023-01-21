from tkinter import *
import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

window = ct.CTk()
window.geometry("320x300")
# window.config(padx=20, pady=20)
window.config(pady=20, padx=20)

timer_label = ct.CTkLabel(text="Timer",
                          text_color="green",
                          text_font=("Ariel", 30),
                          pady=15)

timer_label.grid(row=0, column=0, columnspan=2)


label = ct.CTkLabel(text="00:00",
                    text_font=("Ariel", 30, "bold"))
label.grid(row=1, column=0, columnspan=2)



start = ct.CTkButton(text="Start")
window.config(padx=10)
start.grid(row=2, column=0)

stop = ct.CTkButton(text="Stop")
stop.grid(row=2, column=1)
stop.config(padx=10)


window.mainloop()
