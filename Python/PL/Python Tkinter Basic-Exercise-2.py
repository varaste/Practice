'''
Python tkinter Basic: Exercise-2 with Solution
Write a Python GUI program to import Tkinter package and create a window. 
Set its title and add a label to the window.
'''

import tkinter as tk
parent = tk.Tk()
parent.title("Arya Python tkinter GUI")
first_label = tk.Label(parent, text = "Arya Varaste")
first_label.grid(column = 0, row = 0)
parent.mainloop()