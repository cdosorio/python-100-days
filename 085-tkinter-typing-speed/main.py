import tkinter as tk
from tkinter import END, Entry, StringVar, Text

BACKGROUND_COLOR = "#B1DDC6"
TOTAL_SECONDS = 60

timer = None
words = ''
timer_started = False

def get_words():
    global words
    f = open("words.txt", "r")
    words = f.read()
    words = words.replace('\n', ' ')

def time_is_over():
    print('time_is_over')    
    total_chars = len(sv.get())
    total_words = total_chars//5
    label_result.configure(text=f"CPM: {total_chars} . WPM: {total_words}") 
    entry_user.config(state='readonly')

def reset():
    print('reset')   
    global timer_started
    timer_started = False  
    label_countdown['text'] = TOTAL_SECONDS   
    label_result.configure(text="Type the words here:") 
    entry_user.config(state='normal')
    entry_user.delete(0, END)
    

def countdown(count):      
    label_countdown['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, count-1)
    else:
        time_is_over()
            
def start_countdown():
    print('timer start')
    global timer
    global timer_started
    timer_started = True 
    countdown(TOTAL_SECONDS)

def callback():
    global timer_started
    if timer_started == False :        
        start_countdown()       
    return True

window = tk.Tk()
window.geometry("800x300")  # Size of the window 
window.title('Typing Speed')
font_label1=('times', 12, 'bold')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
sv = StringVar()


# Time left.
label_countdown_caption = tk.Label(window,text='Time left:', font=font_label1)  
label_countdown_caption.grid(row=0, column=0)

label_countdown = tk.Label(window, text=TOTAL_SECONDS, font=font_label1)   
label_countdown.grid(row=0, column=1)

# Button reset
button_reset = tk.Button(window, text='Restart', width=20 ,command = reset)
button_reset.grid(row=0, column=2) 

# Example words
get_words()
txtarea = Text(window, width=90, height=10)
txtarea.grid( row=1, column=0, columnspan=3)
txtarea.insert(END , words)

# label hint and result
label_result = tk.Label(window,text='Type the words here:', font=font_label1)  
label_result.grid(row=2, column=0, columnspan=3)

# user entry
entry_user = Entry(window, font=font_label1, width=90, textvariable=sv, validate="key", validatecommand=callback)
entry_user.grid(row=3, column=0, columnspan=3)



window.mainloop()