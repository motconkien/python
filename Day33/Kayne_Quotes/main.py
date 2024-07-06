import requests
from tkinter import *

API_link = "https://api.kanye.rest"

def get_quotes():
    response = requests.get(API_link)
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text,text = quote)

#UI setup
window = Tk()
window.title("Kenny says...")
window.config(padx=50,pady=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="Day33/Kayne_Quotes/background.png")
canvas.create_image(150,207,image = background_image)
quote_text = canvas.create_text(150,207, text = "", width=250, font=("Arial", 20, "italic"))
canvas.grid(row=0,column=0)

kanye_image = PhotoImage(file = "Day33/Kayne_Quotes/kanye.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, command=get_quotes)
kanye_button.grid(row=1,column=0)

window.mainloop()