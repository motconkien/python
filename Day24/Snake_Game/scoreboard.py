from turtle import Turtle

ALIGHMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day24/data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align= ALIGHMENT, font= FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day24/data.txt", mode = "w") as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGHMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()