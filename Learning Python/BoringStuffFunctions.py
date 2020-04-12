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

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

def spam():
    print(eggs)

eggs = 123
spam()
print(eggs)

def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 42
spam() # sets eggs to 'spam'
print(eggs) # spam

#def spam():#
#    print(eggs)
#    eggs = 'spam local'
#spam()

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument")

print(spam(2))
print(spam(0))
print(spam(4))
