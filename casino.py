import random as ran
money = 200

#game selection
def gameSelection():
    global gameLibrary
    global game
    game = 0
    gameLibrary = ["1"]
    print("""--------------------
Which game will you play?
1) Blackjack""")
    while not game in gameLibrary:
        game = input("<answer>> ")
        if not game in gameLibrary:
            print(f"""{game} is not a valid answer
Try again""")

#games
def playGame(): 
    None
#start
print("""-----------------
Welcome to casino""")
gameSelection()
playGame()
