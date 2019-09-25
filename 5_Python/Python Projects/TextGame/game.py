# Python: 3.7.3
# Author: Jeremiah Davis
# Purpose: Python text based game

def start(nice=0, mean=0, name=""):
    #get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print( "\nThank you for playing again, {}!".format(name) )
    else:
        while True:
            if name == "":
                name = input( "\nWhat is your name? \n>>> ".capitalize() )
                if name != "":
                    print("\nWelcome, {}!".format(name) )
                    print("\nIn this game, you will be greeted \n by several different people.\n")
                    print("but at the end of the game your fate \n will be sealed by your actions.")
                    break
    return name

def nice_mean(nice, mean, name):
    while True: # game loop
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation.  Will you be nice\nor mean? (N/M/quit) \n>>>: ".lower() )
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = nice + 1
            break
        if pick == "m":
            print("The stranger glares at you \nmenacingly and storms off...")
            mean = mean + 1
            break
        if pick == "quit":
            quit()
    score(nice, mean, name) # pass the three variables to the score()

def show_score(nice, mean, name):
    print( "\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean) )

def score(nice, mean, name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice,mean,name)

def win(nice, mean, name):
    print( "\nNice job {}, you win!\n Everyone loves you and you've \n made lots of friends along the way!".format(name) )
    again(nice, mean, name)

def lose(nice, mean, name):
    print( "\nTerrible job {}, you lose!\n Everyone hates you and you've \n made no friends along the way!".format(name) )
    again(nice, mean, name)

def again(nice, mean, name):
    while True:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            reset(nice,mean,name)
            break
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)


# main entry point
if __name__ == "__main__":
    start()
