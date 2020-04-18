birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol':'Mar 4'}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthdays of ' + name)
    else:
        print("I do not have the birthday information for " + name)
        print("What is " + "s birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated")

print(birthdays)
