import random as ran
money = 200

#game selection
def gameSelection():
    global gameLibrary
    global game
    global money
    game = 0
    gameLibrary = ["1"]
    print(f"You have ${money}")
    print("-----------------\nWhich game will you play?\n1) Blackjack")
    while not game in gameLibrary:
        game = input("<answer>> ")
        if not game in gameLibrary:
            print(f"{game} is not a valid answer\nTry again")

#games
def playGame(): 
    None
#start
print("""-----------------
Welcome to Virtual Casino""")
gameSelection()
playGame()
