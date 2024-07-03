from tkinter import * 
from tkinter import messagebox
import random
import json

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
    new_data = {
        web:{
            "email": email,
            "password": password
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        try:
            with open("Day30/data.json","r") as file:
                #read-  update old with new - saving data
                data=json.load(file)
        except FileExistsError:
            with open("Day30/data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("Day30/data.json","w") as file:
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

#FIND_PASSWORD
def find_password():
    web = website_entry.get()

    try:
        with open("Day30/data.json","r") as file:
            data = json.load(file)

    except FileExistsError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for the {web} exists")

# UI SETUP
window = Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_png = PhotoImage(file="Day29/logo.png")
canvas.create_image(100,100,image = logo_png)
canvas.grid(column=1,row=0)

#information holder
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_entry = Entry(width=39)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"hoang@gmail.com")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_button = Button(text ="Generate Password", command=generate_password, width=15)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text = "Search", width= 15, command=find_password, fg="red")
search_button.grid(row=1, column=2)

window.mainloop()