import random

diceRolling = True

while diceRolling:
    print(random.randint(1, 6))

    playAgain = input("Do you want to roll again? [y/n] ")

    if playAgain == "y":
        continue
    else:
        print("GAME OVER!!!")
        break