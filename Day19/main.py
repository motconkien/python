from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtel_index in range(6):
    new_turtel = Turtle(shape="turtle")
    new_turtel.color(colors[turtel_index])
    new_turtel.penup()
    new_turtel.goto(x=-230, y=y_positions[turtel_index])
    all_turtles.append(new_turtel)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win = turtle.pencolor()
            if win == user_bet:
                print("You won")
            else:
                print(f"You lost! The {win} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()