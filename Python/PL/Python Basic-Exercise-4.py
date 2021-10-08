'''
Write a Python program which accepts the radius of a circle from the user and
compute the area.

Python: Area of a Circle

In geometry, the area enclosed by a circle of radius r is πr2. 
Here the Greek letter π represents a constant, approximately equal to 3.14159,
which is equal to the ratio of the circumference of any circle to its diameter.
'''

from math import pi

rad = float(input("Input the radius of the circle: "))
a_circle = (rad**2) * pi
print("The area of the cirvle with radius" + str(rad) + " is: " + str(a_circle))