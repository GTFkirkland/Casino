import random as ran
import time as time
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
#reset
print(reset)
#functions
def line():
    print(f"{bold}-------------------------{reset}")
def showMoney():
    global money
    print(f"You have {bold}{green}${money}{reset}")
def randomCard():
    cardNums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    suits = ["clubs", "hearts", "spades", "diamonds"]
    card = {"num": ran.choice(cardNums), "suit": ran.choice(suits)}
    return card
def loadGame(title):
    print(f"{red}{bold}Running {title}...{reset}")
    time.sleep(ran.randint(65,100)/100)
    print(f"{red}{bold}Success{reset}")
    time.sleep(ran.randint(15,35)/100)

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
    loadGame("Blackjack")
    dealerCards = [randomCard(), randomCard()]
    playercards = [randomCard(), randomCard()]
    print(f'The dealer has a [?] and a {dealerCards[1]["num"]} of {dealerCards[1]["suit"]}')
#game player
def playGame(): 
    global gameLibrary
    global game
    global money
    if game == "1":
        blackjack()

#start
line()
print(f"{red}{bold}Welcome to Virtual Casino{reset}")
gameSelection()
playGame()
