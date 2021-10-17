'''
Python tkinter widgets: Exercise-5 with Solution
Write a Python GUI program to create a Checkbutton widget using tkinter module.
'''

import tkinter as tk
from tkinter import ttk

parent = tk.Tk()
my_boolean_var = tk.BooleanVar()

my_checkbutton = ttk.Checkbutton(
    text="Check when the option True",
    variable=my_boolean_var
)
my_checkbutton.pack()
parent.mainloop()