spam = ['cat', 'dog', 'bat', 'elephant']

print(spam[2])
print(spam[:])
print(spam[-2])
print(spam[1:3])
print(spam[-2:-1])
print(spam[:2])

del spam[2]
print(spam)

catNames = []
while True:
    print("Enter the name of cat number " + str(len(catNames) + 1) + " or enter nothing to stop.:")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print("The cat names are: ")
for name in catNames:
    print(" " + name)

for i in range(10):
    print(str(i))
    i = i+2 # this is ignored!!!!

myList = ["bla", "blbla", "hallo"]
a,b,c = myList
print(a)

import random
spam = ["hi", "hallo", "howdy", "heyas"]
print(str(spam.index("hi")))
print(str(spam.index("heyas")))

messages = ["hi",
    "hallo",
    "zeas",
    "Hej",
    "Hello",
    "Bonjour"]
print(messages[random.randint(0,len(messages) - 1)])

def commaCode(myList):
    l = len(myList)
    myStr = ""
    for i in range(0,len(myList)-1):
        myStr = myStr + str(myList[i]) + ", "
    myStr = myStr + "and " + str(myList[len(myList)-1])
    print(myStr)
commaCode(["hi", "hallo", "howdy", "heyas", 3, 4])

myGrid = [[".", ".", ".",".",".","."],
[".", "0", "0",".",".","."],
["0", "0", "0","0",".","."],
["0", "0", "0","0","0","."],
[".", "0", "0", "0","0","0"],
["0", "0", "0","0","0","."],
["0", "0", "0","0",".","."],
[".", "0", "0",".",".","."],
[".", ".", ".",".",".","."]]

for j in range(0,len(myGrid[0])):
    for i in range(0,len(myGrid)):
        print(myGrid[i][j], end = " ")
    print(" ")
