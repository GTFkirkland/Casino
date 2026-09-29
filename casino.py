import random as ran
#colors
reset = '\033[0m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
cyan = '\033[36m'
bold = '\033[1m'
#variables
money = 200
#functions
print(reset)
def line():
    print(f"{bold}-------------------------{reset}")
def showMoney():
    global money
    print(f"You have {bold}{green}${money}{reset}")
#game selection
def gameSelection():
    global gameLibrary
    global game
    global money
    game = 0
    gameLibrary = ["1"]
    showMoney()
    line()
    print("Which game will you play?\n1) Blackjack")
    while not game in gameLibrary:
        game = input(f"{yellow}{bold}<answer>> ")
        if not game in gameLibrary:
            print(f"{game} is not a valid answer\nTry again")

#games
def blackjack():
    None

#game player
def playGame(): 
    global gameLibrary
    global game
    global money
    if game == 1:
        blackjack()

#start
line()
print(f"{red}{bold}Welcome to Virtual Casino{reset}")
gameSelection()
playGame()
