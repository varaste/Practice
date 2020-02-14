#43

import string

def writeToFile2():
    with open("letters.txt", "w") as file:
        for letter1, letter2 in zip(string.ascii_letters[0::2], string.ascii_letters[1::2]):
            file.write(letter1 + letter2 + "\n")
            print(letter1 + letter2 + "\n")

writeToFile2()
