'''
Python tkinter widgets: Exercise-4 with Solution
Write a Python GUI program to create a Combobox with three options using tkinter module.
'''

import tkinter as tk
from tkinter import ttk


parent = tk.Tk()
parent.geometry('800x450')

my_str_var = tk.StringVar()

my_combobox = ttk.Combobox(parent, textvariable = my_str_var, values=["Face", "Hand", "Body"])

my_combobox.pack()
parent.mainloop()