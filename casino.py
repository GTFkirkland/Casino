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
def determineTotal(cards):
    total = 0
    aces = 0
    for card in cards:
        value = card[:-1]
        if value in ("10", "J", "Q", "K"):
            total += 10
        elif value == "A":
            total += 11
            aces += 1
        else:
            total += int(value)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total
    

def resetDeck():
    global deck
    #make the deck
    deck =[]
    for i in range(2,14):
        if i <= 10:
            deck.append(str(i)+"♤")
            deck.append(str(i)+"♧")
            deck.append(str(i)+"♡")
            deck.append(str(i)+"♢")
        elif i == 11:
            deck.append("J"+"♤")
            deck.append("J"+"♧")
            deck.append("J"+"♡")
            deck.append("J"+"♢")
        elif i == 12:
            deck.append("Q"+"♤")
            deck.append("Q"+"♧")
            deck.append("Q"+"♡")
            deck.append("Q"+"♢")
        elif i == 13:
            deck.append("K"+"♤")
            deck.append("K"+"♧")
            deck.append("K"+"♡")
            deck.append("K"+"♢")
        elif i == 14:
            deck.append("A"+"♤")
            deck.append("A"+"♧")
            deck.append("A"+"♡")
            deck.append("A"+"♢")
    ran.shuffle(deck)
def randomCard():
    global deck
    #random card
    card = deck[0]
    deck.pop(0)
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
        print("Which game will you play?\n 0) Exit\n 1) Blackjack")
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
    #game
    while playerTotal < 21:
        #visuals
        print(f"{bold}Dealer's cards:\n{reset}{cyan} [??][{dealerCards[1]}]{reset}")
        print(f"{bold}Your cards:\n{reset}{cyan} [{playerCards[0]}][{playerCards[1]}]{reset}")
        #input
        #print(playerTotal) #debug
        choice = input(f"{red}{bold}Would you like to hit or stay?{reset}\n{yellow}{bold}<answer>> {reset}")
        #hit, stay, or invalid
        if choice == "hit":
            None
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