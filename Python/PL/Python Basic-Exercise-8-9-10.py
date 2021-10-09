'''
Python Basic: Exercise-8 with Solution
Write a Python program to display the first and last colors from the following list.
'''

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])


'''
Python Basic: Exercise-9 with Solution
Write a Python program to display the examination schedule. (extract the date 
from exam_st_date).
'''

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)


'''
Python Basic: Exercise-10 with Solution
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
'''

n = int(input("Enter yor integer: "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
print(n1 + n2 + n3)