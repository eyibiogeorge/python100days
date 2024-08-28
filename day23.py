import random
def rollDice(sides):
  roll = random.randint(1,sides)
  return roll

while True:
  size = int(input("how many sides"))
  print(rollDice(size))
  tryAgain = input("try again?")
  if tryAgain == "yes":
    continue
  else:
    break