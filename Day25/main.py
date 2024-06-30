import pandas as pd
import turtle 

screen = turtle.Screen()
screen.title("U.S. States Game")
image_path = "Day25/blank_states_img.gif"
screen.addshape(image_path)

turtle.shape(image_path)

data = pd.read_csv("Day25/50_states.csv")

guess_answer = []

while len(guess_answer) < 50:
    answer = screen.textinput(f"{len(guess_answer)}/50 Guess the State", "What is another state's name?").title()
    if answer in data["state"].to_list():
        guess_answer.append(answer)
        position = data[data["state"] == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(position.x), int(position.y))
        t.write(answer)
    
    if answer == "Exit":
        missing_state = []
        for state in data["state"].to_list():
            if state not in guess_answer:
                missing_state.append(state)
        df = pd.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")
        break


