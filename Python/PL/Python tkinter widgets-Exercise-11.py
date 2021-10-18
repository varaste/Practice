'''
Python tkinter widgets: Exercise-11 with Solution
Write a Python GUI program to create a Progress bar widgets using tkinter module.
'''

import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk

parent = tk.Tk()
parent.title("Progressbar")
parent.geometry('350x200')

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='red')

bar = Progressbar(parent, length=220, style='black.Horizontal.TProgressbar')
bar['value'] = 80
bar.grid(column=0, row=0)

parent.mainloop()