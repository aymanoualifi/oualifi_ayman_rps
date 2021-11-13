from random import randint
from gamecomponents import winlose, gameVars, gamecomparison

# set up our game loop so that we can keep playing and not exit
#define a winlose function and invoke it
#when lives run out computer or player

while gameVars.player is False:
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)
  
    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winlose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winlose.winorlose("won")

    gameVars.player = False