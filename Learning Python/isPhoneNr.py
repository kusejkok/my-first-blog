# chapter 7: phone nr without regular expression

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
                return False
    if text[7] != "-":
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
                return False
    return True

print(isPhoneNumber("123-123-1231"))
print(isPhoneNumber("0123-123-1231"))
print(isPhoneNumber("0-123-123-1231"))
print(isPhoneNumber("bla 123-123-1231"))
print(isPhoneNumber("123-12-12316"))
print(isPhoneNumber("123-123-2351"))

message = "Call me 123-123-1111 or at 123-123-1231 tomorrow"

for i in range(len(message)):
    chunk = message[i: i+12]
    if isPhoneNumber(chunk):
        print("Phone number " + chunk)
print("Done")
