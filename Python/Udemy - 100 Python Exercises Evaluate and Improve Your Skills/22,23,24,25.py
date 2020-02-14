#22
from string import ascii_lowercase

d = {
    "a" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "b" : [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "c" : [21, 22, 23, 24, 25, 26, 27, 27, 28, 29, 30]
}
dd = {
    "a" : list(range(1, 11)),
    "b" : list(range(11, 21)),
    "c" : list(range(21,31))
}
print(d)
print(dd)


#23

print(dd["b"][2])


#24

dd = {
    "a" : list(range(1, 11)),
    "b" : list(range(11, 21)),
    "c" : list(range(21,31))
}

print("b has value " , dd["b"])
print("c has value " , dd["c"])
print("a has value " , dd["a"])

print(dd.items())

for key, value in dd.items():
    print(key, "has value ", value)


#25

for letter in ascii_lowercase:
    print(letter)