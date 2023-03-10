#Basic program for checking if inputed number is a vaild phone number

def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not an area code
    if text[3] != '-':
        return False  # does not have first hyphen
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # does not have first 3 digits
    if text[7] != '-':
        return False  # does not have second hyphen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    #Not a loop used for extracting substrings of the message string, SYNTAX: string[start:end]
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')