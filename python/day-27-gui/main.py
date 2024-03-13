from tkinter import *

window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
# padding 
window.config(padx=20, pady=10)

# LABEL

my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label.place(x=200, y=100)

my_label['text'] = 'New Text'
my_label.config(text='Some new Text')
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10);

def button_clicked():
  print('I got clicked')
  new_text = input.get()
  my_label.config(text=new_text)

button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

new_button = Button(text='New button')
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

# def add(*args):
#   sum = 0
#   for n in args:
#     sum += n

#   print(sum)
#   print(args[2])

# add(3, 4, 5)

# def calculate(n, **kwargs):
#   # print(kwargs)
#   # print(type (kwargs))
#   n += kwargs['add']
#   n *= kwargs['multiply']
#   print(n)

# calculate(2, add=3, multiply=5)

# class Car:
  
#   def __init__(self, **kw):
#     self.make = kw.get('make')
#     self.model = kw.get('model')


# my_car = Car(model='GT-R')
# print(my_car.make)

window.mainloop()
