from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# configure flask app to use flask_login
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        
        # hashing and salting the password entered by the user
        hash_and_salted_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=12)
        
        # storing the password in our database
        new_user = User(
            email=request.form['email'],
            name=request.form['name'],
            password=hash_and_salted_password
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # log in and authenticate user after adding details to database
        login_user(new_user)
        
        # can redirect() and get name from the current_user
        return redirect(url_for('secrets'))
    
    # passing True or False if the user is authenticated.
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # find user by email entered
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        # check stored password hash against entered password hashed
        if not user or not check_password_hash(user.password, password):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
        
    # passing True or False if the user is authenticated.
    return render_template("login.html", logged_in=current_user.is_authenticated)

# only logged in users can access this route
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # passing the name from the current user
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True, port=5003)
