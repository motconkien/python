import turtle as tur
import random

tur.colormode(255)
tim = tur.Turtle()
tim.speed(0) #fastes
tim.penup()
tim.hideturtle()

color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),
              (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),
              (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),
              (98, 96, 186)]

color = random.choice(color_list)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot in range(1,number_of_dots+1):
    tim.dot(20,color)
    tim.forward(50)

    if dot %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = tur.Screen()
screen.exitonclick()