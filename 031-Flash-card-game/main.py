from random import choice
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
timer = None
card = None

try:
    df_words_to_learn = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df_words_to_learn = pandas.read_csv("data/french_words.csv")
finally:        
    print(f"Words to learn: {len(df_words_to_learn)}")
    list_cards = df_words_to_learn.to_dict(orient="records") # dataframe to a list of dictionaries  


# ---------------------------- GET NEXT WORD ------------------------------- #
def get_next_card():
    global card, timer
    window.after_cancel(timer)
    card = choice(list_cards) #card is a dict with 2 elems
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")
    timer = window.after(3000, func=flip_card)

def get_next_card_right():
    list_cards.remove(card)
    df = pandas.DataFrame(list_cards)
    df.to_csv("data/words_to_learn.csv", index=False) # index = record number
    get_next_card()

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=image_card_back)
    canvas.itemconfig(card_title, fill="white")
    canvas.itemconfig(card_word, fill="white")
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=card["English"])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card) # simple timer: not required to do a process each second, as a difference to pomodoro timer

canvas = Canvas(width=800, height=526, highlightthickness=0) # same size as image
image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_card_front) # image at center of canvas
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("FONT_NAME", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("FONT_NAME", 60, "bold"))
get_next_card()

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=get_next_card)
button_wrong.grid(column=0, row=1)

image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=get_next_card_right)
button_right.grid(column=1, row=1)



window.mainloop()