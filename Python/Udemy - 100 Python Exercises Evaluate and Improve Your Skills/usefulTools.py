import random

feetInMile = 5280
metersInKilometer = 1000
friends = ["Arya", "Soroush", "Nastaran", "Reza", "Mahdis"]

def getFileExt(fileName):
    return fileName[fileName.index(".") + 1:]

def rollDice(num):
    return random.randint(1, num)
