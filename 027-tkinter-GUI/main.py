from tkinter import *

def button_clicked():
    print("I got clicked")
    label["text"] = input.get()

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label["text"] = "new text"
label.config(text="new text")
label.grid(column=0, row=0) #label.pack()
label.config(padx=20, pady=20)

#Button
button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="Click me")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=20)
input.grid(column=3, row=2)




window.mainloop()