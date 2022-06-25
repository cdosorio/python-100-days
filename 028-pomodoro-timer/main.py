import math
from tkinter import *

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
    canvas.itemconfig(text_timer, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_ticker.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = 10 # WORK_MIN * 60
    short_break_sec = 5# SHORT_BREAK_MIN * 60
    long_break_sec = 10 #LONG_BREAK_MIN * 60        
            
    if reps == 8:
        count_down(long_break_sec)        
        label_timer.config(text="Break", fg=PINK)        
    elif reps % 2 == 0:
        count_down(short_break_sec)        
        label_timer.config(text="Break", fg=GREEN)
    else:
        count_down(work_sec)        
        label_timer.config(text="Work", fg=RED)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count): 

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}" # python is strongly - dinamically typed

    canvas.itemconfig(text_timer, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()

        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range (work_sessions):
            marks += "✓"
        label_ticker.config(text=marks)

        # if (reps % 2 == 0):
        #      current_checks = label_ticker.cget("text")
        #      current_checks += "✓"
        #     label_ticker.config(text=current_checks)

    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", font=("FONT_NAME", 40), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

label_ticker = Label(fg=GREEN, bg=YELLOW) 
label_ticker.grid(column=1, row=3)


window.mainloop()