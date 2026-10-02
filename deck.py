#imports
import random as ran
import time as time

deck =[]
#functions
def determineTotal(cards):
    total = 0
    aces = 0
    for card in cards: 
        if len(card) == 3:
            value = card[0] + card[1]
        else:
            value = card[0]
        if value in ("10", "J", "Q", "K"):
            total += 10
        elif value == "A":
            total += 11
            aces += 1
        else:
            total += int(value)

    while total > 21 and aces > 0:
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
    randomCard = deck[0]
    deck.pop(0)
    return randomCard