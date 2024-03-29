'''
Python tkinter widgets: Exercise-9 with Solution
Write a Python GUI program to create three radio buttons widgets using tkinter module.
'''

import tkinter as tk

parent = tk.Tk()
parent.title("Radiobutton ")
parent.geometry('350x200')

radio1 = tk.Radiobutton(parent, text='First', value=1)
radio2 = tk.Radiobutton(parent, text='Second', value=2)
radio3 = tk.Radiobutton(parent, text='Third', value=3)

radio1.grid(column=0, row=0)
radio2.grid(column=1, row=0)
radio3.grid(column=2, row=0)

parent.mainloop()
