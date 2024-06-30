from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("white")
        self.speed(0)
        self.refresh()
    
    def refresh(self):
        random_x = randint(-280,280)
        random_y = randint(-280,280)
        self.goto(random_x,random_y)

