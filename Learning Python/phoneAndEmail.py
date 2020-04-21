#! python3
# Find phone and mail addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r"""(
    (\+\d{2}|00\d{2})? # area code (optional)
    (\s|-|\.)?            # separator (optional)
    (\d{2})              # first 2 digits
    (\s|-|\.)            # separator
    (\d{3})              # 3 digits
    (\s|-|\.)            # separator
    (\d{2})              # first 2 digits
    (\s|-|\.)            # separator
    (\d{2})              # first 2 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)""", re.VERBOSE)

emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+    # username
    @
    [a-zA-Z0-9.-]+       # domain username
    (\.[a-zA-Z]{2,4})    # dot something
)""", re.VERBOSE)

# Find mathces from clipboard
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5], groups[7], groups[9]])
    if groups[7] != "":
        phoneNum += " x" + groups[10]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("no matches")

# Eg. try the USZ webpage!!!
