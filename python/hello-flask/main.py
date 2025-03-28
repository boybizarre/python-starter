from flask import Flask
import random

RANDOM_NUMBER = random.randint(0,9)
print(RANDOM_NUMBER)

app = Flask(__name__)

@app.route('/')
def home():
  return "<h1>Guess a number between 0 and 9</h1>" \
         "<img src'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"

@app.route('/<int:guess>')
def guess_number(guess):
  if guess > RANDOM_NUMBER:
    return "<h1 style='color: purple'>Too high, try again!</h1>" \
           "<img src'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
  elif guess < RANDOM_NUMBER:
    return "<h1 style='color: red'>Too low, try again!</h1>" \
           "<img src'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
  else:
    return "<h1 style='color: green'>YOU FOUND ME!</h1>" \
           "<img src'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"
    
if __name__ == '__main__':
  app.run(debug=True)