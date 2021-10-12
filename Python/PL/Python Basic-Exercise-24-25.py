'''
Python Basic: Exercise-24 with Solution
Write a Python program to test whether a passed letter is a vowel or not.
'''

def vowel(letter):
    if (letter == "a") or (letter == "e") or (letter == "o") or (letter == "i") or (letter == "u"):
        print("Entered letter is in vowels")
    else:
        print("Vowels letter not found")
        
vowel("a")
vowel("r")
vowel("y")
vowel("v")
vowel("s")
vowel("i")


'''
Python Basic: Exercise-25 with Solution
Write a Python program to check whether a specified value is contained in a 
group of values.

Test Data:
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''
group_of_values = [1 , 3, 7, 0, 5, 9]
def isin_gov(group_of_values, n):
    for value in group_of_values:
        if n == value:
            return True
    return False    

print(isin_gov(group_of_values, 8))
print(isin_gov(group_of_values, 10))
print(isin_gov(group_of_values, 7))


    
    