'''
Python tkinter widgets: Exercise-7 with Solution
Write a Python GUI program to create a Text widget using tkinter module. 
Insert a string at the beginning then insert a string into the current text.
Delete the first and last character of the text.
'''

import tkinter as tk

parent = tk.Tk()
# create the widget.
mytext = tk.Text(parent)

# insert a string at the beginning
mytext.insert('1.0', "- Python exercises, solution -")

# insert a string into the current text
mytext.insert('1.19', ' Practice,')

# delete the first and last character (including a newline character)
mytext.delete('1.0')
mytext.delete('end - 2 chars')
mytext.pack()
parent.mainloop()