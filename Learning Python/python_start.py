# This is a start into Python;
# Katharina Kusejko, 01.04.2020 (no joke).
# Source Webpage: https://tutorial.djangogirls.org/de/python_introduction/

# To run the project, either click on Packages -> Script -> Run Script (installed script package)
# or run over the Console: python3
# with print(), you can directly see the output when running (without, only on Console)
# Let's start

# 1) First Calculations
print(2+3)
print(4*5)
print(5-1)
print(40/2)
print(2**3)

# 2) Strings
print("Ola")
print("Hi, " + "Ola") # Concatenate strings
print("Ola" * 3) #three times the string "Ola"

print("Runnin' down the hill") # version one for ' in string
print('Runnin\' down the hill') # version two for ' in string

print("Ola".upper()) # Apply the methods "upper" to the strings
print(len("Ola")) # length of the string "Ola"
print(len(str(12344))) # str transforms number into string

# 3) Variables
name = "Sonja"
print(name)
print("Der Name " + name + " hat " + str(len(name)) + " Buchstaben.")

a = 4
b = 6
print(a * b)

# 4) List
lottery = [3, 42, 12, 19, 30, 59]
print(len(lottery))
lottery.sort() # sorts in increasing order
print(lottery)
lottery.reverse() # reverses order
print(lottery)
lottery.append(199) # append element to list
print(lottery)
print(lottery[0]) # indices: start with 0!
lottery.pop(1) # removes the 2nd entry
print(lottery)
lottery.pop(-1) # removes last entry
print(lottery)
lottery.pop(-0) # removes first element!!
print(lottery)

# 5) Dictionaries
participant = {'name': 'Kathi', 'country': 'Austria', 'favorite_numbers': [7, 14, 20]}
print(participant['name'])
participant['favorite_language'] = 'Python' # add new entry
print(participant['favorite_language'])
print(len(participant))
participant.pop('favorite_numbers')
print(participant)
participant['country'] = "Switzerland"

# 6) Comparisons
print(5 > 2)
print(3 < 1)
print(5 > 2*3)
print(1 == 1)
print(5 != 2)
print(6 >= 12/2)
print(3 <= 2)
print(6 > 2 and 2 < 3)
print(3 > 2 and 2 < 1)
print(3 > 2 or 2 < 1)

# 7) Boolean
a = True # Careful: True, not TRUE, true...
a = 5 > 2
print(a)
print(True and True)
print(False and True)
print(True and 1 == 1)
print(1 != 2)

# 8) What if...?
if 3 > 2:
    print("It works!")

if 5 > 2:
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")

name = "Kathi"
if name == "Ola":
    print("Hej Ola")
elif name == "Sonja":
    print("Hej Sonja")
else:
    print("Hej anonymous!")

volume = 45
if volume < 20:
    print("Sehr leise")
elif 20 <= volume < 40:
    print("Leise")
elif 40 <= volume < 60:
    print("Perfekt")
elif 60 <= volume < 80:
    print("Laut")
elif 80 <= volume < 100:
    print("Sehr laut")
else:
    print("Ahhhhhhh")

volume = 18
if volume < 20 or volume > 80:
    print(volume)
    volume = 50
    print(volume)
    print("So ist es besser")

# 9) Funktionen
def hallo():
    print("Halli-Hallo")
    print("Wie geht's?")

hallo()

def hallo(name):
    if name == "Ola":
        print("Hej Ola")
    elif name == "Sonja":
        print("Hej Sonja")
    else:
        print("Hej anonymous!")

hallo("Ola")
hallo("Sonja")
hallo("Kathi")

def hallo(name):
    print("Hallo " + name + "!")

hallo("Kathi")

# 10) Loops
girls = ["Rachel", "Monica", "Phoebe", "Ola", "Kathi"]

for name in girls:
    hallo(name)
    print("Naechstes Maedchen")

for i in range(1, 6):
     print(i)
