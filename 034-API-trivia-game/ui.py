from cgitb import text
from textwrap import fill
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text="Score:0", background=THEME_COLOR, foreground="white", font=("arial", 12))
        self.label_score.grid( row=0, column=1)

        self.canvas = Canvas(width=300, height=250) 
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)        
        self.text_quiz = self.canvas.create_text(150, 125, width=280, text="Next question", fill=THEME_COLOR, font=("arial", 20, "italic"))       

        image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=image_true, highlightthickness=0, command=self.is_true)
        self.button_true.grid(row=2, column=0)

        image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.is_false)
        self.button_false.grid(row=2, column=1)
   
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')        
        if self.quiz.still_has_questions():            
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_quiz, text = q_text)
        else:
            self.canvas.itemconfig(self.text_quiz, text = "end of quiz")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def is_true(self):        
        is_right = self.quiz.check_answer("True")        
        self.give_feedback(is_right)

    def is_false(self):        
        is_right = self.quiz.check_answer("False")        
        self.give_feedback(is_right)

    def give_feedback(self, is_right):  
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        
        #self.canvas.update()
        self.window.after(1000, self.get_next_question)
 



