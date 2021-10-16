'''
Python tkinter Basic: Exercise-5 with Solution
Write a Python GUI program to create a window and disable to resize the window 
using tkinter module.
'''

import tkinter as tk

parent = tk.Tk()
parent.title("Arya Python tkinter GUI")
parent.geometry('800x450')
parent.resizable(0,0)

my_label = tk.Label(parent, text="Arya Varaste", font=("Arial Bold", 24))
my_label.grid(column=0, row=0)

parent.mainloop()
