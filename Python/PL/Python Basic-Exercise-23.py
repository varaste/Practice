
'''
Python Basic: Exercise-23 with Solution
Write a Python program to get the n (non-negative integer) copies of the first 
2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2.
'''

def copy2(inpot_string, n):
    if len(inpot_string) < 2:
        p_inpot_string = inpot_string[:2]
        for i in range(n):
            print(p_inpot_string)
    else:
        p_inpot_string = inpot_string[:2]
        for i in range(n):
            print(p_inpot_string)
        
copy2("Arya", 3)
copy2("ry", 3)
copy2("y", 3)
        