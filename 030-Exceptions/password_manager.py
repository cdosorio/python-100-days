import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

NAME = "Courier"
DATA_FILENAME = "data.json"

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
    new_data = {
        website: {
            "email":email,
            "password": passw
        }
    }

    if len(website) == 0 or len(passw)==0:
        messagebox.showinfo(title="Opps", message="Please make sure there is not empty fields!")
    else:   
        try:
          with open(DATA_FILENAME, "r") as file:
            data = json.load(file)  
        except FileNotFoundError:
            with open(DATA_FILENAME, "w") as file:   
                json.dump(data, file, indent=4)
        else:
            data.update(new_data) 
            with open(DATA_FILENAME, "w") as file:   
                json.dump(data, file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()
    if len(website) == 0 :
        messagebox.showinfo(title="Opps", message="Website field is empty")
    else:
        try:
          with open(DATA_FILENAME, "r") as file:
            data = json.load(file)  
        except FileNotFoundError:
            messagebox.showinfo(title="Opps", message="No data file found")
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="Opps", message=f"No details for {website} exists")
            

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
#canvas.pack()

# Row 1
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

input_website = Entry()
input_website.grid(column=1, row=1, sticky="EW")
input_website.focus()

button_add = Button(text="Search", command=find_password)
button_add.grid(column=2, row=1, columnspan=2, sticky="EW")

# Row 2
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

input_email = Entry()
input_email.grid(column=1, row=2, columnspan=2, sticky="EW")
input_email.insert(END , "angela@email.com") # END: last char index

# Row 3
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

input_password = Entry()
input_password.grid(column=1, row=3, sticky="EW")

button_generate = Button(text="Generate password", command=generate_password)
button_generate.grid(column=2, row=3, sticky="EW")

# Row 4
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()