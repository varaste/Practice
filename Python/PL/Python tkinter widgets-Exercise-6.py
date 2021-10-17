'''
Python tkinter widgets: Exercise-6 with Solution
Write a Python GUI program to create a Spinbox widget using tkinter module.
'''

import tkinter as tk

parent = tk.Tk()
text_var = tk.DoubleVar()

spin_box = tk.Spinbox(parent, from_=0.0, to=50.0, increment=1, textvariable=text_var)

spin_box.pack()
parent.mainloop()