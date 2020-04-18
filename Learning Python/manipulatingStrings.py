'''This is a multiline comment.
You can write as many lines you want here.
Doesn't matter
'''

while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number!")

while True:
    print("Select a password: (letters and numbers only)")
    password = input()
    if password.isalnum():
        break
    print("letters and numbers only!!!")

def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, "-"))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth, "."))

picnic1 = {'sandwich':4, 'apples':3, 'bananas':10, 'ice cream': 100}

printPicnic(picnic1, 10, 5)
printPicnic(picnic1, 20, 20)
printPicnic(picnic1, 20, 5)
