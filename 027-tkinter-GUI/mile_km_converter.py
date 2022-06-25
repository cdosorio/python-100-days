from tkinter import *

def button_clicked():    
    miles = input.get()
    kms = float(miles) * 1.609344
    label_result_km["text"] = round(kms , 2)

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=400, height=300)
window.config(padx=10, pady=10)

input = Entry(width=20)
input.grid(column=1, row=0)

label_miles = Label(text="Miles", font=("Arial", 20))
label_miles.grid(column=2, row=0)

label = Label(text="is equal to", font=("Arial", 20))
label.grid(column=0, row=1)

label_result_km = Label(text="0", font=("Arial", 20))
label_result_km.grid(column=1, row=1)

label_kms = Label(text="Km", font=("Arial", 20))
label_kms.grid(column=2, row=1)

button1 = Button(text="Calculate", command=button_clicked)
button1.grid(column=1, row=2)



window.mainloop()