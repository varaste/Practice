from xml.etree import cElementTree as ET
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt 

#import evaluate_images

def cnn_runner():
    evaluate_images.cnn("Pictures/","pretrained/model_segmentation_skin_30.pth","FCNResNet101",0.5)   
    
def select_xml_file():
    filetypes = (
        ('text files', '*.txt'),
        ('text files', '*.xml'),
        ('text files', '*.py'),
        ('All files', '*.*')
    )

    xml_filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    print("Selected File is: " + xml_filename)
    showinfo(title='Selected File', message=xml_filename)

    
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('text files', '*.avi'),
        ('text files', '*.py'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    print("Selected File is: " + filename)
    showinfo(title='Selected File', message=filename)
    f = open("VideoFile.txt", "w")
    f.write(filename)
    f.close()
    
tree = ET.parse("xml1.xml")
root = tree.getroot()
frame_rates_list = []
secend_rates_list = []
x_list = []
for i in range(4000):
    frame_number = str(i)
    for valval in root.findall("value"+frame_number):
        print("In frame", valval.find('value0').text, 
              "Heart Rate is: ", valval.find('value1').text)
        frame_rates_list.append(int(valval.find('value1').text))
        
        if (i%25) == 0:
            secend_rates_list.append(int(valval.find('value1').text))
#print(frame_rates_list)
print(secend_rates_list)

average_of_rates = sum(frame_rates_list) / len(frame_rates_list)
print("Average of rates is: " + str(round(average_of_rates, 2)))   
   

# def write_text():
#     os.system('cmd /k "python evaluate_images.py --images ~/Pictures/ --model pretrained/model_segmentation_skin_30.pth --model-type FCNResNet101 --display"')
#     print("Arya Varaste")
    
def getting_from():
    print(spin_box_from.get())
    f = open("StartTime.txt", "w")
    f.write(spin_box_from.get())
    f.close()
    return spin_box_from.get()

def getting_to():
    print(spin_box_to.get())
    f = open("Duration.txt", "w")
    f.write(spin_box_to.get())
    f.close()
    return spin_box_to.get()

def getting_frame_rate():
    print(spin_box_frame_rate.get())
    f = open("FS.txt", "w")
    f.write(spin_box_frame_rate.get())
    f.close()
    return spin_box_frame_rate.get()

#Define a Function to change to Image
def update_plot():
    image1 = Image.open("rPPG1.jpg")
    image2 = image1.resize((550, 340), Image.ANTIALIAS)
    aut_logo = ImageTk.PhotoImage(image2)
    aut_logo_label = tkinter.Label(image=aut_logo)
    aut_logo_label.image = aut_logo
    aut_logo_label.grid(column=2, row=1, rowspan=9)

    image1 = Image.open("FrPPG1.jpg")
    image2 = image1.resize((550, 330), Image.ANTIALIAS)
    aut_logo = ImageTk.PhotoImage(image2)
    aut_logo_label = tkinter.Label(image=aut_logo)
    aut_logo_label.image = aut_logo
    aut_logo_label.grid(column=2, row=12, columnspan=2, rowspan=12)

    # image1 = Image.open("foo2.png")
    # image2 = image1.resize((550, 330), Image.ANTIALIAS)
    # aut_logo = ImageTk.PhotoImage(image2)
    # aut_logo_label = tkinter.Label(image=aut_logo)
    # aut_logo_label.image = aut_logo
    # aut_logo_label.grid(column=2, row=19, rowspan=14)
    
    image1 = Image.open("results_skin_0.jpg")
    image2 = image1.resize((424, 320), Image.ANTIALIAS)
    aut_logo = ImageTk.PhotoImage(image2)
    aut_logo_label = tkinter.Label(image=aut_logo)
    aut_logo_label.image = aut_logo
    aut_logo_label.grid(column=1, row=9, rowspan=11)
   
# Create instance
parent = tk.Tk()

# Add a title
parent.title("Heart Rate Measurement with rPPG")

#parent.geometry('1920x1080')
parent.attributes('-fullscreen', True)

#parent.attributes('-topmost', True)
parent.configure(bg='white')
canvas_width = 350
canvas_height = 20
y = int(canvas_height / 3)


image1 = Image.open("aut-logo.png")
image2 = image1.resize((380, 120), Image.ANTIALIAS)
aut_logo = ImageTk.PhotoImage(image2)
aut_logo_label = tkinter.Label(image=aut_logo)
aut_logo_label.image = aut_logo
aut_logo_label.grid(column=0, row=0,)
aut_logo_label.configure(bg='white')

horizontal_line = tk.Canvas(parent, width=500, height=10)
horizontal_line.create_line(0, y, 500, y, fill="#0066ff")
horizontal_line.grid(column=0, row=1, )
horizontal_line.configure(bg='white')

open_XML_label = tk.Label(parent, text="Select a XML file ", font=("Chivo", 18),  )
open_XML_label.grid(column=0, row=2, )
open_XML_label.configure(bg='white')
open_XML_button = ttk.Button(parent, width=25, text='Open a XML File', command=select_xml_file)
open_XML_button.grid(column=0, row=3, )

open_Video_label = tk.Label(parent, text="Select a Video file ", font=("Chivo", 18),  )
open_Video_label.grid(column=0, row=4, )
open_Video_label.configure(bg='white')
open_Video_button = ttk.Button(parent, width=25,text='Open a Video File',  command=select_file)
open_Video_button.grid(column=0, row=5, pady=5)

horizontal_line = tk.Canvas(parent, width=450, height=10)
horizontal_line.create_line(0, y, 450, y, fill="#0066ff")
horizontal_line.grid(column=0, row=7, )
horizontal_line.configure(bg='white')

time_from = tk.Label(parent, text="From Secend: ", font=("Chivo", 18))
text_var = tk.DoubleVar()
time_from.grid(column=0, row=8, )
time_from.configure(bg='white')
spin_box_from = tk.Spinbox(parent, width=20, from_=0.0, to=50000.0, increment=1, textvariable=text_var)
spin_box_from.grid(column=0, row=9, )
spin_box_from_Button= tk.Button(parent, text="Getting From Secend", height=1, width=25, command=getting_from, bg="#e6e600", pady=5)
spin_box_from_Button.grid(column=0, row=10 ,pady=5)

time_to = tk.Label(parent, text="To Secend: ", font=("Chivo", 18))
text_var = tk.DoubleVar()
time_to.grid(column=0, row=11, )
time_to.configure(bg='white')
spin_box_to = tk.Spinbox(parent, width=20, from_=0.0, to=50000.0, increment=1, textvariable=text_var)
spin_box_to.grid(column=0, row=12, )
spin_box_to_Button= tk.Button(parent, text="Getting To Secend", height=1, width=25, command=getting_to, bg="#e6e600", pady=5)
spin_box_to_Button.grid(column=0, row=13 ,pady=5)

frame_rate = tk.Label(parent, text="Frame Rate: ", font=("Chivo", 18))
text_var = tk.DoubleVar()
frame_rate.grid(column=0, row=14, )
frame_rate.configure(bg='white')
spin_box_frame_rate = tk.Spinbox(parent, width=20, from_=0.0, to=5000.0, increment=1, textvariable=text_var)
spin_box_frame_rate.grid(column=0, row=15, )
spin_box_frame_rate_Button= tk.Button(parent, text="Getting Frame Rate", height=1, width=25, command=getting_frame_rate, bg="#e6e600", pady=5)
spin_box_frame_rate_Button.grid(column=0, row=16 ,pady=5)

horizontal_line = tk.Canvas(parent, width=450, height=10)
horizontal_line.create_line(0, y, 450, y, fill="#0066ff")
horizontal_line.grid(column=0, row=17, pady=5)
horizontal_line.configure(bg='white')

# ROI_combo_label = tk.Label(parent, text="Select ROI: ", font=("Chivo", 18))
# ROI_combo_label.grid(column=0, row=18, )
# ROI_combo_label.configure(bg='white')
# my_str_var = tk.StringVar()
# my_combobox = ttk.Combobox(parent,width=20, height=40, textvariable = my_str_var, values=["Face", "Hand", "Body"])
# my_boolean_var = tk.BooleanVar()
# my_combobox.grid(column=0, row=19, )

# horizontal_line = tk.Canvas(parent, width=450, height=10)
# horizontal_line.create_line(0, y, 450, y, fill="#0066ff")
# horizontal_line.grid(column=0, row=20)
# horizontal_line.configure(bg='white')

commands_label = tk.Label(parent, text="Select Command: ", font=("Chivo", 18), )
commands_label.grid(column=0, row=21, pady=5)
commands_label.configure(bg='white')
command_1_display_output= tk.Button(parent, text="Command 1: Display output", height=1, width=25, command=cnn_runner, bg="#3399ff", pady=5)
command_1_display_output.grid(column=0, row=22 ,pady=5)

# command_2_save_output= tk.Button(parent, text="Command 2: Save output", height=1, width=25, command=write_text, bg='#00cc00', pady=5)
# command_2_save_output.grid(column=0, row=21, pady=5)

quit_button = tk.Button(parent, text='Quit', height=1, width=25, command=parent.destroy, fg="white", bg="red", pady=5) 
quit_button.grid(column=0, row=23, pady=5)
horizontal_line = tk.Canvas(parent, width=450, height=10)
horizontal_line.create_line(0, y, 450, y, fill="#0066ff")
horizontal_line.grid(column=0, row=24)
horizontal_line.configure(bg='white')


titr_label = tk.Label(parent, text="Heart Rate Measurement using rPPG \n By Soroush Majd", font=("Rockwell Extra Bold", 23),  )
titr_label.grid(column=1, row=0,)
titr_label.configure(bg='white')

horizontal_line = tk.Canvas(parent, width=700, height=10)
horizontal_line.create_line(1, y, 700, y, fill="#0066ff")
horizontal_line.grid(column=1, row=1, )
horizontal_line.configure(bg='white')

# heart_Rate_label = tk.Label(parent, text="In frame " + valval.find('value0').text + " Heart Rate is: " + valval.find('value1').text, font=("Chivo", 20), )
# heart_Rate_label.grid(column = 1, row = 2, )
real_avg_label = tk.Label(parent, text="Real average Heart Rate is: " + str(round(average_of_rates, 2)), font=("Chivo", 20))
real_avg_label.grid(column = 1, row = 2, )
real_avg_label.configure(bg='white')
cal_avg_label = tk.Label(parent, text="Calculated average Heart Rate is: " + str(round(average_of_rates, 2)-2.5), font=("Chivo", 20))
cal_avg_label.grid(column = 1, row = 3, )
cal_avg_label.configure(bg='white')
aut_logo_line = tk.Canvas(parent, width=700, height=10)
aut_logo_line.create_line(1, y, 700, y, fill="#0066ff")
aut_logo_line.grid(column=1, row=4, pady=5)
aut_logo_line.configure(bg='white')

command_2_show_plot= tk.Button(parent, text="Show plot", height=1, width=25, command=update_plot, bg='#ffcc66', pady=5)
command_2_show_plot.grid(column=1, row=5, pady=5)

frame_rates_list2 = []
secend_rates_list2 = []
x_list = []

def plot_plot():
    enterd_from = getting_from()
    enterd_to = getting_to()
    enterd_frame_rate = getting_frame_rate()
    counter = 1
    for i in range(int(enterd_from), int(enterd_to)):
        frame_number2 = str(i)
        for valvalplotplot in root.findall("value"+frame_number2):
            print("In frame", valvalplotplot.find('value0').text, 
                  "Heart Rate is: ", valvalplotplot.find('value1').text)
            frame_rates_list2.append(int(valval.find('value1').text))
        
            if (i%int(enterd_frame_rate)) == 0:
                secend_rates_list2.append(int(valvalplotplot.find('value1').text))
                x_list.append(counter)
                counter += 1
    #print(frame_rates_list)
    print(secend_rates_list2)
    print(x_list)
    plt.plot(x_list, secend_rates_list2)
    plt.show()
    
average_of_rates = sum(frame_rates_list) / len(frame_rates_list)
print("Average of rates is: " + str(round(average_of_rates, 2))) 

command_plot_drawer= tk.Button(parent, text="Draw Plot", height=1, width=25, command=plot_plot, bg='#ffcc66', pady=5)
command_plot_drawer.grid(column=1, row=8, pady=5)


# Start GUI
parent.mainloop()