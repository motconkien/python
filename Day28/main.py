from tkinter import *
import math

#CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#TIMER RESET
def reset_time():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text = "00:00")
    check_marks.config(text = "")
    global reps 
    reps = 0
    

#TIMER MECHANISM
def start_time():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60 

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg= RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg= PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg= YELLOW)
        

#COUNTDOWN MECHANISM
def countdown(count):
    count_minute = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_minute}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_time()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark+= "✔"
        check_marks.config(text=mark)

#UI SETUP
window = Tk()
window.title("MY POMODORO")
window.config(padx=100,pady=50, background=GREEN)

timer_label = Label(text= "TIMER",font=(FONT_NAME,32, "bold"),foreground=YELLOW,bg=GREEN)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224, bg=GREEN,highlightthickness=0)
tomato_png = PhotoImage(file="Day28/tomato.png")
canvas.create_image(100,112,image = tomato_png)

timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

#button
start_button = Button(text="Start",highlightthickness=0, command=start_time)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_time)
reset_button.grid(column=2,row=2)

check_marks = Label(fg=YELLOW,bg=GREEN)
check_marks.grid(column=1,row=3)

window.mainloop()