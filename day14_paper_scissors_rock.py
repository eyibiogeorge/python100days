from getpass import getpass as input
print("player 1: ")
player1 = input("enter R for Rock, S for scissors, P for paper: ")
print()
print("player 2: ")
player2 = input("enter R for Rock, S for scissors, P for paper: ")

print()
if player1.lower() == "r" and player2.lower() == "s":
    print(f"Rock beat Scissors")
elif player1.lower() == "p" and player2.lower() == "s":
    print(f"Scissors beat Paper")

elif player1.lower() == "r" and player2.lower() == "p":
    print(f"Paper beat Rock")
elif player1.lower() == player2.lower():
    print("Game is a tie")
else:
    print("invalid input")