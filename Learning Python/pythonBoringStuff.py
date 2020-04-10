
## Chapter 1
# Variable names in python: letters and numbers and _, not starting with a number!

# This program says hallo, asks for the name and age
print('Hello!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is ' + str(len(myName)))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in one year.')

## Chaper 2: Flow control
print('What is your name again?')
name = input()
if name == 'kathi':
    print('Hi, Kathi')
elif name == 'Christian':
    print('Hi, Christian')
else:
    print('Who are you?')

i = 1
while i < 10:
    print(str(i))
    i = i + 1

name = ''
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

import random
for i in range(5):
    print(random.randint(1,10))
