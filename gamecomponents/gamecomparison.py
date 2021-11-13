from gamecomponents import gameVars

 def gamecomparison(computer):
    print("computer chose:" + gamecomparison.computer)


  if gamecomparison.computer == gameVars.player:
        # tie - nothing else to compare, so it'll exit
        print("tie! try again")

    elif gameVars.player == "rock":
        if gamecomparison.computer == "paper":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if gamecomparison.computer == "scissors":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if gamecomparison.computer == "rock":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1
