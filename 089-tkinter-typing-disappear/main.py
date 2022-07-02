import tkinter as tk
from tkinter import END, Text

BACKGROUND_COLOR = "#B1DDC6"
MAX_SECONDS = 5

timer = None

def time_is_over():
    print('time_is_over')    
    txtarea.delete('1.0', END)
    
def reset():
    print('reset')   
    label_countdown['text'] = MAX_SECONDS  
    txtarea.delete('1.0', END) 

def countdown(count):      
    label_countdown['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        global timer
        window.after_cancel(timer)
        timer = window.after(1000, countdown, count-1)
    else:
        time_is_over()
            
def key_pressed(ev=None):
    #restart timer with every key  
    print("key_pressed")     
    countdown(MAX_SECONDS)  
    return True

window = tk.Tk()
window.geometry("800x300")  # Size of the window 
window.title('Dangerous Writing Prompt')
font_label1=('times', 12, 'bold')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(1000000, countdown, MAX_SECONDS) # wait a loong time at begining!

# Time left.
label_countdown_caption = tk.Label(window,text='Time left:', font=font_label1)  
label_countdown_caption.grid(row=0, column=0)

label_countdown = tk.Label(window, text=MAX_SECONDS, font=font_label1)   
label_countdown.grid(row=0, column=1)

# Button reset
button_reset = tk.Button(window, text='Restart Timer', width=20 ,command = reset)
button_reset.grid(row=0, column=2) 

# Input area 
txtarea = Text(window, width=90, height=10)
txtarea.grid( row=1, column=0, columnspan=3)
txtarea.bind("<KeyRelease>", key_pressed)

# label hint
label_hint = tk.Label(window,text=f'if you stop for more than {MAX_SECONDS} seconds, everything will be deleted', font=font_label1, fg='#f00')  
label_hint.grid(row=2, column=0, columnspan=3)



window.mainloop()