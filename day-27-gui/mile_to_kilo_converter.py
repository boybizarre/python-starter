from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Kilo Converter")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)

def miles_to_kilometer():
  miles = float(miles_input.get())
  km = round(miles * 1.609)
  result_label.config(text=f'{km}')

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text='0')
result_label.grid(column=1, row=1)

kilometer_label = Label(text='Km')
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)


















window.mainloop()
