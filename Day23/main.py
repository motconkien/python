from turtle import Screen
import time
from car import Cars
from scoreboard import Scoreboard
from player import Player

player = Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkey(player.up,"Up")

score = Scoreboard()
cars = Cars()


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            score.game_over()
        
    if player.is_finish_line():
        player.go_to_start()
        cars.level_up()
        score.increase_score()
    

screen.exitonclick()