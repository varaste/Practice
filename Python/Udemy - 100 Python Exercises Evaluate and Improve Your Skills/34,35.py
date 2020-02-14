#34

def foo():
    global c
    c = 1
    return c
foo()
print(c)


#35

def wordCount():
    inS = input("Enter String: ")
    inList = inS.split(" ")
    print(inList)
    inListLen = len(inList)
    print(inListLen)

wordCount()


