answer = input("Do you want to play this game? [yes/no]: ")

if answer == "yes":
    print("WELCOME to the game.")
    answer = input("Do you want to go Jungle or Cave? [jungle / cave]: ")

    if answer == "jungle":
        print("You see the hungry Tiger. Tiger will eat you. Game CLOSED!!!")

    elif answer == "cave":
        print("You see the Bear in front of cave.")
        answer = input("Do you want to fight with the bear or run away? [fight / run]")

        if answer == "fight":
            print("Bear is too much strong. You loose the GAME!!!")

        else:
            print("WOW!!! Still you are alive.")

else:
    print("The game is CLOSED!!!")

