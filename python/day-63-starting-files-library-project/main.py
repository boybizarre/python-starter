import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT OR REPLACE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

#  create the app
app = Flask(__name__)

# Create the database
class Base(DeclarativeBase):
    pass

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# create the extension
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all()
    
# CREATE RECORD
# new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=9.3)
# db.session.add(new_book)
# db.session.commit()

all_books = []

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title= request.form['title'],
            author= request.form['author'], 
            rating= request.form['rating'] 
        )

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        # UPDATE RECORD
        book_id = request.form['id']
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        
        return redirect(url_for('home')) 
    
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit_rating.html', book=book_selected)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)

    # Alternative way to select the book to delete
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    
    db.session.delete(book_to_delete)
    db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

# # reading all records
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
    
# # reading a partcular record by query
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == 'Harry Potter')).scalar()

# # update a particular record by query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == 'Harry Potter')).scalar()
#     book_to_update.title = 'Harry Potter and the Chamber of Secrets'
#     db.session.commit()

# # update record by primary key
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = 'Harry Potter and the Goblet of Fire'
#     db.session.commit()
    
    