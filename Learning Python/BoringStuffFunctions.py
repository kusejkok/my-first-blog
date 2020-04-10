# Chapter 3: Functions

def hallo():
    print("Hallo")
    print("Hej")

hallo()

def hallo(name):
    print("Hallo " + str(name))

hallo("Kathi")

import random

def magic(ranNr):
    if ranNr == 1:
        return "Yes"
    elif ranNr == 2:
        return "Well...."
    elif ranNr == 3:
        return "blabla"
    else:
        return "gagagag"

myNr = random.randint(1,10)
fortune = magic(myNr)
print(fortune)

#spam = print("Hallo")
print('cats', 'mice')
