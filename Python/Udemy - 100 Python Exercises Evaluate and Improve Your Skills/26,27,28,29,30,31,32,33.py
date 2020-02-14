import math

#26

for num in range(1, 11):
    print(num)


#27

def acceleration(v1, v2, t1, t2):
    acc = (v2 - v1) / (t2 - t1)
    print("acceleration is: ", acc)
    return acc

acceleration(0, 10, 0, 20)


#28

def foo(a, b):
    return a + b

x = foo(2, 3) * 10


#29

def  liquidVolumeInaSphere(r, hc):
    liquidVolume = ((4 * math.pi * r**3) / 3) - ((math.pi * hc**2 * ((3 * r)-hc) / 3))
    print(liquidVolume)

liquidVolumeInaSphere(10, 2)


#30

def foo(b, a=2):
    return a + b
#Hint: Always put non default parameters first followed by default ones.


#31

def foo(a=1, b=2):
    c = a + b
    return c

x = foo() - 1
print(x)


#32

c = 1
def foo():
    return c
c = 3
print(foo())


#33

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

