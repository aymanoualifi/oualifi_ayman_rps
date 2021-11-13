from gamecomponents import gameVars


def gameResult(computer):
    print("Computer chose: " + computer)

    if (computer == gameVars.player):
        print("A tie? Try again!")

    elif (gameVars.player == "rock"):
        if (computer == "paper"):
            print("you lost!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("nice!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "paper"):
        if (computer == "scissors"):
            print("you lost!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You're killing it!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "scissors"):
        if (computer == "rock"):
            print("You lost!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("Good one!")
            gameVars.computerLives = gameVars.computerLives - 1


