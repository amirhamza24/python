word = "Hablu"
chances = 5
guessAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guessAdd:
            print(letter, end = " ")
        else:
            print("_", end = "")

    myGuess = input(f"Your Chances is: {chances}, guess the letter: ")

    guessAdd.append(myGuess.lower())

    if myGuess.lower() not in word.lower():
        chances = chances - 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guessAdd:
            done = False

if done:
    print(f"YES.. You have won the game, the word is: {word}")

else:
    print("SORRY.. You loose the game.")