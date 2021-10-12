'''
Python Basic: Exercise-27 with Solution
Write a Python program to concatenate all elements in a list into a string and return it.
'''

def concat(list):
    output = ""
    for element in list:
        output = output + str(element)
    return output

print(concat([1, 4, 0, 0,"/" , 0, 7,"/" ,2, 0]))


'''
Python Basic: Exercise-28 with Solution
Write a Python program to print out all even numbers from a given numbers list 
in the same order and stop the printing if any numbers that come after 237 in 
the sequence.
'''

numbers_list = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for n in numbers_list:
    if n == 237:
        print (n)
        break;
    elif n % 2 == 0:
        print(n)

'''
Python Basic: Exercise-29 with Solution
Write a Python program to print out a set containing all the colors from 
color_list_1 which are not present in color_list_2.

Test Data:
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
'''
list1 = set(["White", "Black", "Red"])
list2 = set(["Red", "Green"])

def is_in_color_list(list1, list2):
    output_list = list1.difference(list2)
    return output_list
  
print(is_in_color_list(list1, list2))
print(is_in_color_list(list2, list1))






