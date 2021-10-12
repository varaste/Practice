'''
Python Basic: Exercise-22 with Solution
Write a Python program to count the number 4 in a given list.
'''

number_list = [10, 8, 7, 6, 2, 4, 9, 4, 19, 14, 11, 4]

four_count = 0

for i in number_list:
    if i == 4:
        four_count = four_count + 1
    else:
        four_count = four_count
        
print(four_count)


    





