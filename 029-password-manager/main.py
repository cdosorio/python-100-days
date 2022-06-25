from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

NAME = "Courier"
DATA_FILENAME = "data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_email.get()
    passw = input_password.get()

    if len(website) == 0 or len(email) or len(passw):
        messagebox.showinfo(title="Opps", message="Please make sure there is not empty fields!")
    else:
        is_ok = messagebox.askokcancel(title = website, message=f"Are you sure to save {email}")

        if is_ok:
            with open(DATA_FILENAME, "a") as file:
                file.write(f"{website}|{email}|{passw}\n")
                #clear 
                input_website.delete(0, END)
                input_email.delete(0, END)
                input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)
#canvas.pack()

label_website = Label(text="Website:")
label_website.grid(column=0, row=2)

input_website = Entry(width=35)
input_website.grid(column=1, row=2, columnspan=2)
input_website.focus()

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=3)

input_email = Entry(width=35)
input_email.grid(column=1, row=3, columnspan=2)
input_email.insert(END , "angela@email.com") # END: last char index

label_password = Label(text="Password:")
label_password.grid(column=0, row=4)

input_password = Entry(width=21)
input_password.grid(column=1, row=4)

button_generate = Button(text="Generate password", command=generate_password)
button_generate.grid(column=2, row=4)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=5, columnspan=2)



window.mainloop()