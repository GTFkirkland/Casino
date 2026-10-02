#imports
import random as ran
import time as time
from deck import determineTotal, resetDeck, randomCard
#colors and symbals
reset = '\033[0m'
red = '\033[31m' #system
green = '\033[32m' #money
yellow = '\033[33m' #input
blue = '\033[34m' #information
cyan = '\033[36m' #cards
bold = '\033[1m'
#variables
money = 200
#reset
print(reset)
#functions
def line(size):
    if size == 0:
        print(f"{bold}-------------------------{reset}")
    elif size == 1:
        print(f"{bold}+=======================+{reset}")
    elif size == 2:
        print(f"{bold}[[[[[[[[[[[[[]]]]]]]]]]]]{reset}")
def showMoney():
    global money
    print(f"You have {bold}{green}${money}{reset}")
def loadGame(title):
    print(f"{red}{bold}Running {title}...{reset}")
    time.sleep(ran.randint(65,100)/100)
    print(f"{red}{bold}Success{reset}")
    time.sleep(ran.randint(15,35)/100)
    line(1)

#game selection
def gameSelection():
    global gameLibrary
    global game
    global money
    game = 0
    gameLibrary = ["0", "1"]
    showMoney()
    line(1)
    print(f"{bold}Which game will you play?\n 0) Exit\n 1) Blackjack")
    game = input(f"{yellow}{bold}<answer>> {reset}")
    if not game in gameLibrary:
        print(f'"{yellow}{bold}{game}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
        time.sleep(ran.randint(65,100)/100)
    while not game in gameLibrary:
        line(0)
        print(f"{bold}Which game will you play?\n 0) Exit\n 1) Blackjack")
        game = input(f"{yellow}{bold}<answer>> {reset}")
        if not game in gameLibrary:
            print(f'"{yellow}{bold}{game}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            time.sleep(ran.randint(65,100)/100)

#games
def blackjack():
    #setup
    loadGame("Blackjack")
    resetDeck()
    playerCards = [randomCard(), randomCard()]
    dealerCards = [randomCard(), randomCard()]
    playerTotal = determineTotal(playerCards)
    #bet
    betValid = False
    while not betValid == True:
        showMoney()
        bet = input(f"{bold}{red}How much will you bet?\n{yellow}<answer>> {reset}")
        try:
            if int(bet) < 1 or int(bet) > money:
                print(f'"{yellow}{bold}{bet}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
                time.sleep(ran.randint(65,100)/100)
                line(0)
            else:
                betValid = True
                time.sleep(ran.randint(65,100)/100)
                line(1)
        except:
            print(f'"{yellow}{bold}{bet}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            time.sleep(ran.randint(65,100)/100)
            line(0)
    #game
    while playerTotal < 21:
        #visuals
        print(f"{bold}Dealer's cards:\n{reset}{cyan} [??][{dealerCards[1]}]{reset}")
        cardMessage = ""
        for i in playerCards:
            cardMessage += "[" + i + "]"
        print(f"{bold}Your cards:\n{reset}{cyan} {cardMessage}{reset}")
        #input
        #print(playerTotal) #debug
        choice = input(f"{red}{bold}Would you like to hit or stay?{reset}\n{yellow}{bold}<answer>> {reset}")
        #hit, stay, or invalid
        if choice == "hit":
            time.sleep(ran.randint(65,100)/100)
            line(1)
            playerCards.append(randomCard())
            playerTotal = determineTotal(playerCards)
        elif choice == "stay":
            break
        else:
            print(f'"{yellow}{bold}{choice}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            time.sleep(ran.randint(65,100)/100)
            line(0)
    if playerTotal > 21:
        print(f"{bold}Dealer's cards:\n{reset}{cyan} [{dealerCards[0]}][{dealerCards[1]}]{reset}")
        cardMessage = ""
        for i in playerCards:
            cardMessage += "[" + i + "]"
        print(f"{bold}Your cards:\n{reset}{cyan} {cardMessage}{reset}")
        print(f"{red}{bold}You busted & lost {green}${bet}{reset}")
    
    
        
        

#game player
def playGame(): 
    global gameLibrary
    global game
    global money
    if game == "0":
        line(1)
        print(f"{red}{bold}Exiting Virtual Casino...{reset}")
        time.sleep(ran.randint(65,100)/100)
        print(f"{red}{bold}Success{reset}")
        time.sleep(ran.randint(15,35)/100)
    elif game == "1":
        blackjack()

#start
line(2)
print(f"{red}{bold}Welcome to Virtual Casino{reset}")
gameSelection()
playGame()