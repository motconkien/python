from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

app = Flask(__name__)
app.secret_key='something'

"""wtforms allows create form without doing manually in html, validators to require user input and can not leave invalid value"""
"""DataRequired is used to validation"""

#set up default email and password
default_email = 'admin@gmail.com'
password = '12345678'

class Myfrom(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email(allow_empty_local=False)])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label='Login')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods =['POST','GET']) #in this route, show the log in place and also get infor from that
def login():
    form = Myfrom()
    if form.validate_on_submit():
        input_email = form.email.data
        input_password = form.password.data
        if input_email == default_email and input_password == password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html',form=form)


if __name__=='__main__':
    app.run(debug=True)