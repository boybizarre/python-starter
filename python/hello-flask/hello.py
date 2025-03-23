from flask import Flask
import random

app = Flask(__name__)

print(__name__)
print(random.__name__)

def make_bold(function):
  def wrapper_func():
    return "<b>" + function() + "</b>"

  return wrapper_func

def make_emphasis(function):
  def wrapper_func():
    return "<em>" + function() + "</em>"

  return wrapper_func

def make_italic(function):
  def wrapper_func():
    return "<i>" + function() + "</i>"
  return wrapper_func

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is a paragraph</p>" \
            "<img src='https://media.giphy.com/media/140ObFj9MRjRIc/giphy.gif?cid=790b76115o0qay91ln44k2qqqv2ufz8cv4fewlp24mbe3d0i&ep=v1_gifs_search&rid=giphy.gif&ct=g' />"

@app.route('/bye')
@make_bold
@make_emphasis
@make_italic
def say_bye():
    return 'BYE!'


@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return f"<h1 style='text-align:center, color: orangered'>Hello there, {name} and you are {age} years old</h1>"

@app.route('/name/<path:name>')
def say_hello(name):
    return f"Saying hello to {name}"

if __name__ == '__main__':
    app.run(debug=True) 