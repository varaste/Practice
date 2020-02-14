#14
a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

#15
varaste = {
    "a" : 1,
    "b" : 2
}
print(varaste)

sina = dict(a = 1, b = 2)
print(sina)

#16
print(sina["b"])

#17
d = {"a": 1, "b": 2, "c": 3}
print(d["a"] + d["b"] + d["c"])

#18
# NULL

#19
d = {"a": 1, "b": 2}
d["3"] = 3
d["4"] = 4
print(d)

#20
d = {"a": 1, "b": 2, "c": 3}
dValue = d.values()
print(sum(dValue))

#21
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

