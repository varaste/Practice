'''
Python tkinter Basic: Exercise-4 with Solution
Write a Python GUI program to create a window and set the default window size 
using tkinter module.
'''

import tkinter as tk
parent = tk.Tk()
parent.title("Arya Python tkinter GUI")
parent.geometry('800x450')
my_label = tk.Label(parent, text="Arya Varaste", font=("Arial Bold", 24))
my_label.grid(column=0, row=0)
parent.mainloop()
