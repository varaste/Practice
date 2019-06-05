# Type your code here
sen = input("Please Enter Yor Age: ")
intsen = int(sen)

if intsen <= 0:
    print("UNBORN")
elif intsen > 0 and intsen <= 150:
    print("ALIVE")
else:
    print("VAMPIER")
    