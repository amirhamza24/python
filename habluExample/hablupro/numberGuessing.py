import random

randomNumber = random.randrange(1, 3
                                )

userInput = int(input("Guess the number: "))

if userInput > randomNumber:
    print(f"Our number is: {randomNumber}")
    print(f"Your number is: {userInput}. Sorry, your number is HIGH. Better luck next time.")

elif randomNumber > userInput:
    print(f"Our number is: {randomNumber}")
    print(f"Your number is: {userInput}. Sorry, your number is LOW. Better luck next time.")

else:
    print(f"Our number is: {randomNumber}")
    print(f"Your number is: {userInput}. CONGRATS. Your number is MATCHED..")