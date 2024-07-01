from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer.config(text = f"{km}")

window = Tk()
window.title("Mile to Kilometer converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row = 0)

miles_label = Label(text = "Miles")
miles_label.grid(column=2, row = 0)

is_equal_label = Label(text = "is equal to")
is_equal_label.grid(column=0, row=1)

kilometer = Label(text = "0")
kilometer.grid(column=1, row = 1)

kilometer_label = Label(text = "KM")
kilometer_label.grid(column=2, row = 1)

calculate_buton = Button(text="Calcualate", command=miles_to_km)
calculate_buton.grid(column=1, row = 2)


window.mainloop()
