import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df_states = pandas.read_csv("50_states.csv")
all_states = df_states.state.to_list()
guessed_states = []

while len(guessed_states) < len(df_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # save missing states to csv
        #missing_states = df_states[~df_states.state.isin(guessed_states)]["state"]
        #print(type(missing_states))                
        missing_states = [state for state in all_states if state not in guessed_states ] # with list comprehension
        df_missing_states = pandas.DataFrame(missing_states)
        df_missing_states.to_csv("missing_states.csv")

        #selectiong multiple colulmns using ising
        found_states = df_states.loc[df_states.state.isin(guessed_states),['state','x'] ]
        print(type(found_states))
        found_states.to_csv("found_states.csv")
        break

    found_state = df_states[df_states.state == answer_state]    
    if not found_state.empty:
        #new turtle to write state
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(found_state.x), int(found_state.y))   
        t.write(f"{found_state.state.item()}", align=ALIGNMENT, font=FONT)
        guessed_states.append(found_state.state.item())



turtle.mainloop()