n = int(input("Please Enter a Integer: "))

if ((n % 3) == 0) and ((n % 2) == 0):
    print("BOTH")
elif (((n % 3) != 0) and ((n % 2) == 0)) or (((n % 3) == 0) and ((n % 2) != 0)):
    print("ONE")
else:
    print("NEITHER")
