def generatePin(pinLenght):
    import random
    pin = ''
    for i in range(pinLenght):
        pin +=str(random.randint(0,9))
    return pin
print(generatePin(15))