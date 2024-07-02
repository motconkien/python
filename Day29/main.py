from tkinter import * 
from tkinter import messagebox
import random

# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letter = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password_list = [random.choice(letters) for _ in range(nr_letter)] 
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)

# SAVE PASSWORD
def save():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title = web, message=f"There are the details entered: \n Email: {email} \n "
                                                    f"Password: {password}\n Is this okay to save?")
        
        if is_ok:
            with open("Day29/data.txt","a") as file:
                file.write(f"{web} | {email} | {password} \n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        

# UI SETUP
window = Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_png = PhotoImage(file="Day29/logo.png")
canvas.create_image(100,100,image = logo_png)
canvas.grid(column=1,row=0)

#information holder
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"hoang@gmail.com")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_button = Button(text ="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()