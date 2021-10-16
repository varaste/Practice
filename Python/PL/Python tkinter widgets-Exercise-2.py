'''
Python tkinter widgets: Exercise-2 with Solution
Write a Python GUI program to add a canvas in your application using tkinter module.
'''

import tkinter as tk 

parent = tk.Tk() 
parent.geometry('800x450')

canvas_width = 500
canvas_height = 200
w = tk.Canvas(parent, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")

parent.mainloop()