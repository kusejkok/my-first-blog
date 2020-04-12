import random

def guess(secNr):
    count = 0
    print("Guess: ")
    guess = input()
    guess = int(guess)
    while guess != secNr:
        if guess > secNr:
            print("Too high")
            count = count + 1
        else:
            print("Too low")
            count = count + 1
        print("Guess: ")
        guess = input()
        guess = int(guess)
    print("Correct, you needed " + str(count) + " attempts")
#guess(5)

def collatz():
    print("Enter a positive integer:")
    myNr = input()
    try:
        myNr = int(myNr)
        while myNr > 1:
            print(str(myNr))
            if myNr % 2 == 0:
                myNr = myNr/2
            else:
                myNr = 3*myNr + 1
            print(str(myNr))
    except ValueError:
        print("Invalid entry")

collatz()
