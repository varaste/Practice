letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])
print(letters[3:6])
print(letters[:3])
print(letters[-4:-1])
#[start:end:step]
'''When you don't pass a step, Python assumes the step is 1. [:]
itself means get everything from start to end. So, [::2]
means get everything from start to end at a step of two'''
print(letters[::2])

