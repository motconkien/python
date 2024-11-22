from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdfgtp'

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary warnings


# Define base class for models
# class Base(declarative_base()):
#     pass
db = SQLAlchemy(app)
# Define Book model
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Define the Book form
class BookForm(FlaskForm):
    bookName = StringField('Book Name', validators=[DataRequired()])
    bookAuthor = StringField('Book Author', validators=[DataRequired()])
    bookRating = StringField('Rating')
    submit = SubmitField('Add Book')

# Home route - display all books
@app.route('/')
def home():
    books = Book.query.all()  # Fetch books from the database
    return render_template('index.html', allbooks=books)

# Add book route
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        bookname = form.bookName.data
        bookauthor = form.bookAuthor.data
        rating = form.bookRating.data

        # Convert rating to float (handle invalid input)
        try:
            rating = float(rating)
        except ValueError:
            return "Invalid rating value", 400
        
        # Create new book entry in the database
        new_book = Book(title=bookname, author=bookauthor, rating=rating)
        try:
            db.session.add(new_book)
            db.session.commit()
            print("Book added successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            return f"Error: {e}", 400
        
        return redirect(url_for('home'))
    
    return render_template('add.html', form=form)

# Delete book route
@app.route("/delete")
def delete():
    # Get the title of the book to delete
    book_title = request.args.get("title")
    if not book_title:
        return "Book title is required", 400

    # Query the database for the book by title
    book_to_delete = Book.query.filter_by(title=book_title).first()
    if not book_to_delete:
        return "Book not found.", 404

    # Delete the book
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not already created
    app.run(debug=True)
