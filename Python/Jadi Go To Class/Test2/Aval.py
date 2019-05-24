x = int(input("EAN: "))
# print(x)
c = 5
aa = []
while c != 0:
    a = x % 10
    aa.append(a)
    x //= 10
    c -=1
print(aa)
b = sum(aa)
print(b)


def bthOdd(q):
    return (2 * q - 1)
print(bthOdd(b))


#
# n = 89
#
# def sum_digits(n):
#     s = 0
#     while n:
#         s += n % 10
#         n //= 10
#     return s
# print(n)

