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
def delay():
    time.sleep(ran.randint(65,100)/100)
#game selection
def gameSelection():
    global gameLibrary
    global game
    global money
    game = 0
    gameLibrary = ["0", "1"]
    line(1)
    showMoney()
    print(f"{bold}Which game will you play?\n 0) Exit\n 1) Blackjack")
    game = input(f"{yellow}{bold}<answer>> {reset}")
    if not game in gameLibrary:
        print(f'"{yellow}{bold}{game}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
        delay()
    while not game in gameLibrary:
        line(0)
        print(f"{bold}Which game will you play?\n 0) Exit\n 1) Blackjack")
        game = input(f"{yellow}{bold}<answer>> {reset}")
        if not game in gameLibrary:
            print(f'"{yellow}{bold}{game}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            delay()

#games
def blackjack():
    global money
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
            if int(bet) > 0 and int(bet) <= money:
                betValid = True
                delay()
                line(1)
            else:
                print(f'"{yellow}{bold}{bet}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
                delay()
                line(0)
        except:
            print(f'"{yellow}{bold}{bet}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            delay()
            line(0)
    #game
    while playerTotal < 21:
        #visuals
        print(f"{bold}Dealer's cards:\n{reset}{cyan} [??][{dealerCards[1]}]{reset}")
        cardMessage = ""
        for i in playerCards:
            cardMessage += "[" + i + "]"
        print(f"{bold}Your cards:\n{reset}{cyan} {cardMessage}{reset}")
        #print(playerTotal) #debug
        #input
        choice = input(f"{red}{bold}Would you like to hit or stay?{reset}\n{yellow}{bold}<answer>> {reset}")
        #hit, stay, or invalid
        if choice == "hit":
            delay()
            line(1)
            playerCards.append(randomCard())
            playerTotal = determineTotal(playerCards)
        elif choice == "stay":
            break
        else:
            print(f'"{yellow}{bold}{choice}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            delay()
            line(0)
    #end
    if playerTotal > 21:
        print(f"{bold}Dealer's cards:\n{reset}{cyan} [{dealerCards[0]}][{dealerCards[1]}]{reset}")
        cardMessage = ""
        for i in playerCards:
            cardMessage += "[" + i + "]"
        print(f"{bold}Your cards:\n{reset}{cyan} {cardMessage}{reset}")
        print(f"{red}{bold}You busted & lost {green}${bet}{reset}")
        money -= bet
    else:
        line(1)
        #player
        print(f"{bold}Your final hand:\n{reset}{cyan} {cardMessage}{reset}")
        delay()
        #dealer
        dealerTotal = determineTotal(dealerCards)
        if dealerTotal < playerTotal:
            #hit
            while dealerTotal < playerTotal:
                dealerCards.append(randomCard())
                dealerTotal = determineTotal(dealerCards)
            if dealerTotal > 21:
                #player win (dealer busted)
                line(0)
                cardMessage = ""
                for i in dealerCards:
                    cardMessage += "[" + i + "]"
                print(f"{bold}Dealer's final hand:\n{reset}{cyan} {cardMessage}{reset}")
                delay()
                print(f"{red}{bold}The dealer busted\nYou win {green}${bet}{reset}")
                money += int(bet)                
            else:
                #dealer win (dealer got high enough)
                line(0)
                cardMessage = ""
                for i in dealerCards:
                    cardMessage += "[" + i + "]"
                print(f"{bold}Dealer's final hand:\n{reset}{cyan} {cardMessage}{reset}")
                delay()
                print(f"{red}{bold}The dealer beat your hand\nYou lost {green}${bet}{reset}")
                money -= int(bet)
        else:
            #dealer win (auto)
            line(0)
            cardMessage = ""
            for i in dealerCards:
                cardMessage += "[" + i + "]"
            print(f"{bold}Dealer's final hand:\n{reset}{cyan} {cardMessage}{reset}")
            delay()
            print(f"{red}{bold}The dealer beat your hand\nYou lost {green}${bet}{reset}")
            money -= int(bet)
    
    
        
        

#game player
def playGame(): 
    global gameLibrary
    global game
    global money
    if game == "0":
        line(1)
        print(f"{red}{bold}Exiting Virtual Casino...{reset}")
        delay()
        print(f"{red}{bold}Success{reset}")
        time.sleep(ran.randint(15,35)/100)
    elif game == "1":
        blackjack()

#start
line(2)
print(f"{red}{bold}Welcome to Virtual Casino{reset}")
gameSelection()
while True:
    playGame()