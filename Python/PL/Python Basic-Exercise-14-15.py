'''
Python Basic: Exercise-14 with Solution
Write a Python program to calculate number of days between two dates.
Python datetime.date(year, month, day):
The function returns date object with same year, month and day. 
All arguments are required. Arguments may be integers, in the following ranges:
MINYEAR <= year <= MAXYEAR
1 <= month <= 12
1 <= day <= number of days in the given month and year
If an argument outside those ranges is given, ValueError is raised.
Note: The smallest year number allowed in a date or datetime object. MINYEAR is 1.
The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
'''

from datetime import date
f_date = date(2021, 8, 10)
l_date = date(2021, 10, 8)
delta = l_date - f_date
print(delta.days)


'''
Python Basic: Exercise-15 with Solution
Write a Python program to get the volume of a sphere with radius 6.
Python: Volume of a Sphere
A sphere is a three-dimensional solid with no face, no edge, no base and no vertex. 
It is a round body with all points on its surface equidistant from the center. 
The volume of a sphere is measured in cubic units.
The volume of the sphere is : V = 4/3 × π × r3 = π × d3/6
'''

from math import pi
radius1 = float(input("Enter Sphere radius: "))
volume = (4/3)*(pi*(radius1**3))
print("The volume of the sphere is: ", volume)
