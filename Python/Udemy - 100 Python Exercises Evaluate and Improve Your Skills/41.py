#41

from string import ascii_letters

def writeToFile():
    file = open("aryaFile.txt", "x")
    for letter in ascii_letters:
        file.write(letter)
        file.write("\n")
        print(letter)

writeToFile()

'''
Explanation:
The ascii_lowercase property of the string  module is quite helpful here to generate 
a string of all letters. 
Then we create a file and while the file is open, 
we iterate through the string and apply the write method in each iteration to write 
the letters in the text file. 
We are also appending \n  to each letter which is a special character that creates break lines. 
That makes sure to separate the letters in different lines.
'''