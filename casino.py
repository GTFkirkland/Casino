import random as ran
import time as time
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
def line():
    print(f"{bold}-------------------------{reset}")
def showMoney():
    global money
    print(f"You have {bold}{green}${money}{reset}")
def randomCard():
    cardNums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♤", "♧", "♡", "♢"]
    card = {"num": ran.choice(cardNums), "suit": ran.choice(suits)}
    if card["num"] == "J" or card["num"] == "Q" or card["num"] == "K":
        card["value"] = 10
    elif card["num"] == "A":
        card["value"] = 11
    else:
        card["value"] = int(card["num"])
    return card
def loadGame(title):
    print(f"{red}{bold}Running {title}...{reset}")
    time.sleep(ran.randint(65,100)/100)
    print(f"{red}{bold}Success{reset}")
    time.sleep(ran.randint(15,35)/100)
    line()

#game selection
def gameSelection():
    global gameLibrary
    global game
    global money
    game = 0
    gameLibrary = ["0", "1"]
    showMoney()
    while not game in gameLibrary:
        line()
        print("Which game will you play?\n0) Exit\n1) Blackjack")
        game = input(f"{yellow}{bold}<answer>> {reset}")
        if not game in gameLibrary:
            print(f'"{yellow}{bold}{game}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            time.sleep(ran.randint(65,100)/100)

#games
def blackjack():
    #setup
    loadGame("Blackjack")
    unavailableCards = []
    dealerCards = [randomCard(), randomCard()]
    playerCards = [randomCard(), randomCard()]
    #totals
    playerTotal = playerCards[0]["value"] + playerCards[1]["value"]
    dealerTotal = dealerCards[0]["value"] + dealerCards[1]["value"]
    #unavailable cards
    unavailableCards.append(dealerCards[0])
    unavailableCards.append(dealerCards[1])
    unavailableCards.append(playerCards[0])
    unavailableCards.append(playerCards[1])
    
    #game
    while playerTotal < 21:
        #ace check
        if playerCards[0]["num"] == "A" or playerCards[1]["num"] == "A" and playerTotal > 21:
            playerTotal -= 10
        #visuals
        print(f"{bold}Dealer's cards:\n{reset}{cyan} [??][{dealerCards[0]['num']}{dealerCards[0]['suit']}]{reset}")
        cardMessage = ""
        for x in playerCards:
            cardMessage += "[" + str(x["num"]) + str(x["suit"]) + "]"
        print(f"{bold}Your cards:\n{reset}{cyan}{" " + cardMessage}{reset}")
        #input
        print(playerTotal)
        choice = input(f"{red}{bold}Would you like to hit or stay?{reset}\n{yellow}{bold}<answer>> {reset}")
        #hit, stay, or invalid
        if choice == "hit":
            playerCards.append(randomCard())
            while playerCards[len(playerCards)-1] in unavailableCards:
                playerCards[len(playerCards)-1] = randomCard()
            playerTotal += playerCards[len(playerCards)-1]["value"]
        elif choice == "stay":
            break
        else:
            print(f'"{yellow}{bold}{choice}{reset}" is not a valid answer\n{red}{bold}Try again{reset}')
            time.sleep(ran.randint(65,100)/100)
            line()
    if playerTotal > 21:
        print(f"{red}{bold}You busted and lost your bet{reset}")
    
    
        
        

#game player
def playGame(): 
    global gameLibrary
    global game
    global money
    if game == "0":
        line()
        print(f"{red}{bold}Exiting Virtual Casino...{reset}")
        time.sleep(ran.randint(65,100)/100)
        print(f"{red}{bold}Success{reset}")
        time.sleep(ran.randint(15,35)/100)
    elif game == "1":
        blackjack()

#start
line()
print(f"{red}{bold}Welcome to Virtual Casino{reset}")
gameSelection()
playGame()