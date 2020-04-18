allGuests = {'Alice': {'apples':5, 'pretzels':12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1, 'pretzels': 5},
             'Kathi': {'cake': 1, 'apples': 3},
             'Christian': {'ham sandwiches': 3}}

def totalBroughts(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

allItems = []
for k in allGuests.values():
    for j in k.keys():
        if j not in allItems:
            allItems.append(j)

for i in allItems:
    print(i + ": " + str(totalBroughts(allGuests, i)))

#### Fantasy game:
myGoods = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print("Inventary:")
count = 0
for k,v in myGoods.items():
    print(str(v) + " " + k)
    count = count + v
print("Total: " + str(count))

myList = ['rope', 'torch', 'rope', 'gold coin', 'gold coin']

def addToInventary(dict, newItems):
    for i in myList:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

addToInventary(myGoods, myList)
print(myGoods)
