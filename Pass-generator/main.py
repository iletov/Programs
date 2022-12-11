import json
from tkinter import messagebox
from tkinter import *
import random
# import customtkinter as ct
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    pass_input.delete(0, END)

    numb = random.randint(5, 8)

    password_letters = [random.choice(letters) for _ in range(numb)]
    password_numbers = [random.choice(numbers) for _ in range(numb)]

    password_list = password_letters + password_numbers

    random.shuffle(password_list)

    final_pass = "".join(password_list)
    # final_pass = ""
    # for x in password_list:
    #     final_pass += x

    pass_input.insert(0, final_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Incorrect data", message="Need to fill all fields")
    else:
        # yeas = messagebox.askyesno(title="confirm", message=f"Website: {website}\n"
        #                                                     f"Email: {email}\n"
        #                                                     f"Password: {password}\n")
        # if yeas:

        try:
            with open("data.json", "r") as file:
                # read the old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                data = json.dump(new_data, file, indent=4)

        else:
            # update with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # save the updated data
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

def find_password():

    search_website = website_input.get()
    try:
        with open("data.json", "r") as json_file:
            json_dict = json.load(json_file)

    except FileNotFoundError:
        pass
    else:
        if search_website in json_dict:
            email_dict = json_dict[search_website]["email"]
            pass_dict = json_dict[search_website]["password"]
            messagebox.showinfo(title="Search box", message=f"email: {email_dict}\n"
                                                            f"pass: {pass_dict}")
        elif search_website not in json_dict:
            messagebox.showinfo(title="Oops, something's wrong!",
                                message="No data to display")
    finally:
        website_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image_png = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=image_png)
canvas.grid(row=0, column=1)

# -----------labels----------
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)

pass_text = Label(text="Password:")
pass_text.grid(row=3, column=0)

# ------------Entry----------
website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "letov88@gmail.com")

pass_input = Entry(width=33)
pass_input.insert(0, "")
pass_input.grid(row=3, column=1)

# -------------Buttons--------
button_pass = Button(text="Generate Password", command=password_generator)
button_pass.grid(row=3, column=2)

button_add = Button(text="Add", width=44, command=save_info)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="Search", width=15, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()