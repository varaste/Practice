'''
Python tkinter widgets: Exercise-1 with Solution
Write a Python GUI program to add a button in your application using tkinter module.
'''

import tkinter as tk 

parent = tk.Tk() 
parent.title('Title - button') 
parent.geometry('800x450')

my_button = tk.Button(parent, text='Quit', height=1, width=20, command=parent.destroy) 
my_button.pack() 
my_button.grid(column=2, row=1)

parent.mainloop()