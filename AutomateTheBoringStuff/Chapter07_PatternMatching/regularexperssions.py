# This is the project to extract phon numbers and email addresses using regix commands

# Project can be broken down into these steps
# 1) Get the text off the clipboard
# 2) Find all the phone numbers and email addresses in the text
# 3) Paste them onto the clipboard


#Part 1 creating the regex for the phone numbers

#Package used for copying text and holding in a buffer
import pyperclip
import re

#Create the regix pattern for a phone number
phoneNumPattr = r'(\d{3})[- ]?(\d{3})[- ]?(\d{4})'

#Create the regix pattern for an email
emailPattr = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Complie the variables with the .compile method to turn them into objects
phoneNumPattrobj = re.compile(r'''(\d{3})[- ]?(\d{3})[- ]?(\d{4})''',re.VERBOSE)
emailPattrobj    = re.compile(r'''\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}\b''',re.VERBOSE)

#Part 2 finding the pattern and pasting the contents from the buffer

text = str(pyperclip.paste())

matchs = []


#Loop through the text
for groups in phoneNumPattrobj.findall(text):
    #Using the join method to join the extracted list of the tuples of numbers from the forloop variable groups[]
    print(groups)
    phonenum = '-'.join([groups[0],groups[1],groups[2]])
    #If statment is used to add a X if there is an extension such as x1234
    if groups[2] != '':
        phonenum += 'x' + groups[2]
    #Append the string to the matchs list
    matchs.append(phonenum)
#Loop for email
for groups in emailPattrobj.findall(text):
    #This is not taking whole string
    print(groups)
    matchs.append(groups[0])



#Part 3 Copy results to clip board

if len(matchs) > 0:
    pyperclip.copy('\n'.join(matchs))
    print('\n'.join(matchs))




