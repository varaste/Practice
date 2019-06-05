# Type your code here
inp = input("Enter a Number: ")
sec = int(inp)
minutes = (sec // 60)
hours = (minutes // 60)
days = hours // 24
sec = sec - (minutes * 60)
minutes = minutes - (hours * 60)
hours = hours - (days * 24)
print(int(days), "days", int(hours), "hours", int(minutes), "minutes", int(sec), "seconds")