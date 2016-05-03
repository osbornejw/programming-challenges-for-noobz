import random

myList=["heads", "tails"]

userGuess = raw_input("Guess heads or tails\n")
coinFlip = random.choice(myList)
if userGuess in myList:
    if userGuess == coinFlip:
        print ("You're right! It was " + coinFlip)
    else:
        print ("Too bad! It was " + coinFlip)
else:
    print "Error, input not found!"
