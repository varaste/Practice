'''
Python Basic: Exercise-26 with Solution
Write a Python program to create a histogram from a given list of integers.
'''

def histogram(histo_int):
    for n in histo_int:
        output = ""
        times = n
        while (times > 0):
            output = output + "֎"
            times = times - 1
        print(output)
        
histogram([1, 3, 7, 7, 0, 5, 1, 9])
histogram([1, 4, 0, 0, 0, 7, 2, 0])
