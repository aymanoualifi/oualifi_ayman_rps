from gamecomponents import gameVars

def winorlose(status):
    print("you " + status)

    choice = input("do you want to play again? y/n: ")

    if choice == "n":
        print("========= hard luck! ==========")
        exit()
    elif choice == "y":
        gameVars.playerLives = 2
        gameVars.computerLives = 2
        gameVars.player = False 