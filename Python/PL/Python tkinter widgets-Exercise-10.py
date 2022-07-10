'''
Python tkinter widgets: Exercise-10 with Solution
Write a Python GUI program to create a ScrolledText widgets using tkinter module.
'''

import tkinter as tk
import tkinter.scrolledtext as tkst

parent = tk.Tk()
parent.title("Scrolledtext")
parent.geometry('350x200')

txt = tkst.ScrolledText(parent, width=40, height=10)
txt.grid(column=0, row=0)

parent.mainloop()