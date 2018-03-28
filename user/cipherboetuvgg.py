#after having done this ages ago i have now forgotten how everything works :P
MAX_KEY_SIZE = 26

#encrypt or decrypt option
def getMode():
    while True:
        print('Do you want to encrypt or decrypt a message, idiot?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('either "encrypt" or "e" or "decrypt" or "d".')

#gets the encrypt or decrypt message
def getMessage():
    print('Enter the message, idiot:')
    return input()
#gets the key
def getKey():
    key = 0
    while True:
        print('Enter the key number you idiot (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

#decrypts
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

#should loop over each letter if it works
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

#uppercase and lowercase stuff
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
#should return the correct translation
            translated += chr(num)
        else:
            translated += symbol
    return translated

#gets mode, message, and key from the user
mode = getMode()
message = getMessage()
key = getKey()

#prints the translated message
print('Your translation is:')
print(getTranslatedMessage(mode, message, key))

