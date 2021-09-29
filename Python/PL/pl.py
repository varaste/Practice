message = 'Arya Varaste'

print(message)
print("The message len is:", len(message))
print("The message first char is:", message[0])
print(message[2:7])
print(message[:7])
print(message[2:])
print(message.lower())
print(message.upper())
print(message.count('ar'))
print(message.find('ar'))
print(message.find('sina'))

Smessage = message.replace("Arya", "Sina")
print(message)
print(Smessage)

Varastes = message + ", " + Smessage
print(Varastes)



