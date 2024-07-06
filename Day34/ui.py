from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg = "white")
        self.score_label.grid(row = 0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Hello", 
            font=("Arial",20,"italic"), 
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_image = PhotoImage(file="Day34/images/true.png")
        false_image = PhotoImage(file="Day34/images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0, command = self.false_pressed)
        self.true_button.grid(row = 2, column=0)
        self.false_button.grid(row = 2, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "Reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self,is_right):
        if is_right:
            # self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        
        self.window.after(1000, func=self.get_next_question)



