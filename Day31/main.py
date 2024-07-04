from tkinter import *
import random
import pandas as pd
import time
BACKGROUND_COLOR = "#B1DDC6"
FRENCH_FONT = ("Ariel", 40, "italic")
ENGLISH_FONT = ("Ariel", 60, "bold")

word_random = {}
word_dict = {}
try:
    df = pd.read_csv("Day31/data/word_to_learn.csv")
except FileNotFoundError:
    orgininal_data = pd.read_csv("Day31/data/french_words.csv")
    word_dict = orgininal_data.to_dict(orient="records")
else:
    word_dict = df.to_dict(orient="records")


# CREATE NEW FLASH CARDS
def next_card():
    global word_random, flip_timer
    window.after_cancel(flip_timer)
    word_random = random.choice(word_dict)
    canvas.itemconfig(canvas_title,text = "French", fill = "black")
    canvas.itemconfig(canvas_word, text = word_random["French"], fill = "black")
    canvas.itemconfig(canvas_image, image = front_image)
    flip_timer = window.after(3000,func = flip_card)
    
#CREATE FLIP the Cards
def flip_card():
    canvas.itemconfig(canvas_image, image = back_image)
    canvas.itemconfig(canvas_title, text = "English")
    canvas.itemconfig(canvas_word, text = word_random["English"], fill = "white")

#CREATE WORD TO LEARN 
def is_known():
    word_dict.remove(word_random)
    data = pd.DataFrame(word_dict)
    data.to_csv("Day31/data/word_to_learn.csv", index=False)
    next_card()


# UI SET UP
window = Tk()
window.title("My Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)
# --create canvas----
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="Day31/image/card_front.png")
back_image = PhotoImage(file="Day31/image/card_back.png")
canvas_image= canvas.create_image(400, 263, image=front_image)
canvas_title = canvas.create_text(400, 150, text="", font=FRENCH_FONT, fill="black")
canvas_word = canvas.create_text(400, 263, text="", font=ENGLISH_FONT, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# ---create button----
right_image = PhotoImage(file="Day31/image/right.png")
wrong_image = PhotoImage(file="Day31/image/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
