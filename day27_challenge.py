import time, os
import random
def characterName(charName):
    return charName

def characterType(charType):
    return charType

def charHealthStat():
    import random
    rollDice1 = random.randint(1,6)
    rollDice2 = random.randint(1,12)
    return  ((rollDice1 * rollDice2)/2)+10

def charHealthStren():
    import random
    rollDice1 = random.randint(1,6)
    rollDice2 = random.randint(1,12)
    return  ((rollDice1 * rollDice2)/2)+12
charName1 = ""
charName2 = ""
healthStren1 =charHealthStren()
healthStren2 =charHealthStren()
healthStat1 =charHealthStat()
healthStat2 =charHealthStat()

print("Character Builder")
print()

print("Enter a name for player1: ")
charName1=input("> ")
print("Character Type (Human, Elf, Wiard, Orc): ")
charType1=input("> ")
print()
print("Enter a name for player2: ")
charName2=input("> ")
print("Character Type (Human, Elf, Wiard, Orc): ")
charType1=input("> ")
time.sleep(2)

print(f'The worries are \n Name: {charName1}\n Health: {healthStat1} \nStrength: {healthStren1}\n\nName: {charName2}\n Health: {healthStat2} \nStrength: {healthStren2}')

counter = 0

while True:
    counter +=1
    print(f"rolling dice {counter} ...")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f'The worries are \n Name: {charName1}\n Health: {healthStat1} \nStrength: {healthStren1}\n\nName: {charName2}\n Health: {healthStat2} \nStrength: {healthStren2}')
    
    if dice1>dice2:
        healthStren2 -=abs(healthStren1-healthStren2) +1
    else:
        healthStren1 -=abs(healthStren1-healthStren2) +1
    if healthStren2 <= 0:
        print(f'{charName1} = {healthStren1} is a winner')
        break
    elif healthStren1 <= 0:
        print(f'{charName2} = {healthStren2} is a winner')
        break
    else:
        continue
    



