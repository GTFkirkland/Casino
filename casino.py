import random as ran
#start function
def intro():
    game = 0
    print("""-----------------
Welcome to casino
-----------------
Which game will you play?
1) Blackjack""")

    while not game > 0 and not game <= 1:
        try:
            game = int(input("<answer>> "))
        except ValueError:
            print(f"""{game} is not a valid answer
                  Try again""")

intro()
