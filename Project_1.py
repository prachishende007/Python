# Snake, Water, Gun
import random

comp = random.choice([-1, 0, 1])

youDict = {"s": 1, "p": -1, "r": 0}

str = input("Enter your choice:")
you = youDict[str]

reverseDict = {1 : "scissor", -1 : "paper", 0 : "rock"}

print(f"You chose {reverseDict[you]}\nand the computer chose {reverseDict[comp]} ")

if((comp - you) == -1 or (comp - you) == 2):
    print("You lose")

elif(comp == you):
    print("Draw")

else:
    print("You win!")
