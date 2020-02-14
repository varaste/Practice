import re
import math

#37

def cammaWordCount():
    cammafile = open("words2.txt", "r")
    readcamma = cammafile.read()
    print(readcamma.replace(",", " ").split(" "))
    print(len(readcamma.replace(",", " ").split(" ")))

cammaWordCount()

'''Explanation 1:
This solution is like the solution of the previous exercise with the difference that 
before splitting we are replacing all commas with a space which will let the split
method count the number of words.
'''
def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)

print(count_words("words2.txt"))

'''Explanation 2:
This alternative solution uses the built-in re  module which provides regular expression
matching operations. We're using the split method of that module and the expression
 ",| " is meant to replace commas with spaces. 
Using methods from the re  module can be more appropriate than Python built-in methods
when string operations are complicated. 
However, for this simple scenario the re  module could be skipped.
'''
def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)

print(count_words_re("words2.txt"))


#38

print(math.sqrt(9))


#39

print(math.cos(1))


#40

print(math.pow(2,4))
'''
If you didn't understand the error, you could do help(math.pow)  to see how the method works.
'''

