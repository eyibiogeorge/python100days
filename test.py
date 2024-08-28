import random

bingo = []

for i in range(8):
    bingo.append(random.randint(10,90))
    
bingo.sort()
print(f'{[bingo[0],bingo[1],bingo[2]]}\n{[bingo[3],"bingo",bingo[4]]}\n{[bingo[5],bingo[6],bingo[7]]}')

    