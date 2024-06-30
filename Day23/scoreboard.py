from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGHMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-270,250)
        self.hideturtle()
        self.score = 0
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align= "left" , font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align= ALIGHMENT, font = FONT)

    def increase_score(self):
        self.score +=1 
        self.clear()
        self.update_score()