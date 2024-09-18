from flask import Flask, render_template, request,redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdfgtp'


class BookForm(FlaskForm):
    bookName = StringField('Book Name',validators=[DataRequired()])
    bookAuthor = StringField('Book Author', validators=[DataRequired()])
    bookRating = StringField('Rating')
    submit = SubmitField('Add Book')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add():
    form = BookForm()
    if form.validate_on_submit():
        bookname = form.bookName.data
        bookauthor = form.bookAuthor.data
        rating = form.bookRating.data
    
        data = [bookname,bookauthor,rating]
        print(data)
    
    return render_template ('add.html',form = form)

if __name__ =='__main__':
    app.run(debug=True)