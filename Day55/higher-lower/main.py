from flask import Flask
import random

number = random.randint(0,9)
print(number)
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnltN2xramw1bXVtaDA4dmgzdDFxZTVvNno2azl3cHhpMW5qcmhtNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/B2Ga6vfzF8T6rJWuut/giphy.gif'/>"
    

@app.route("/<int:guess>")
def guess_number(guess):
    if guess == number:
        return "<h1 style = 'color:green'> You found me </h1>"\
                "<img src = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjVuaXZpNW90OGFrZDdrbWx4NXJjNWk3YjN0Zmk3MTNlb2hlcTlmOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yJFeycRK2DB4c/giphy.gif'/>"
    
    elif guess < number:
        return "<h1 style = 'color: red'>Too low, try again</h1>"\
                "<img src = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3R6am5xd256bnB4Ympqem9tZm56ZHdoZTFkZmRhbDI0dHEyYXNyYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kka4uG2ts5wdndJgPO/giphy.gif'/>"
    else:
        return "Too high, try again"\
                "<img src = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDhjZGxvcW4xNG94MGlubXQwcm5zZjN1cjN0enIxMXV1cWVucHcxaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UFRtykmfyBA8F7qPh9/giphy.gif'/>"

if __name__=="__main__":
    app.run(debug=True)