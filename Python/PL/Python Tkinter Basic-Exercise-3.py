'''
Python tkinter Basic: Exercise-3 with Solution
Write a Python GUI program to create a label and change the label font style 
(font name, bold, size) using tkinter module.
'''

import tkinter as tk
parent = tk.Tk()
parent.title("Arya Python tkinter GUI")
my_label = tk.Label(parent, text="Arya Varaste", font=("Arial Bold", 24))
my_label.grid(column=0, row=0)
parent.mainloop()
