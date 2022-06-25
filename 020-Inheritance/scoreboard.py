from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
DATA_FILENAME = "data.txt"

class Scoreboard(Turtle):

    def __init__(self) :
        super().__init__()        
        self.score = 0
        self.high_score = self.read_high_score()        
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()    

    def update_scoreboard(self):   
        self.clear()     
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self) :
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        with open(DATA_FILENAME) as file:
            score = int(file.read())            
            return score
            

    def save_high_score(self):
        with open(DATA_FILENAME, "w") as file:
            file.write(str(self.high_score))

