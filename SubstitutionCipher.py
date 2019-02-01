#-------------Encryption and Decryption -------------#

import  sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
  print("Substitution Cipher")
  print ("1.Encryption")
  print ("2.Decryption")
  mode=int(input("Choose Mode"))
  if (mode==1):
    mode='encrypt'
  if (mode==2):
    mode='decrypt'
  message=input("Enter message")
  key=input("Enter Key")
  cipher(message,key ,mode)

def cipher(message,key,mode):
  myMessage = message
  myKey = key
  myMode = mode # set to 'encrypt' or 'decrypt'
  checkValidKey(myKey)
  if myMode == 'encrypt':
    translated = encryptMessage(myKey, myMessage)
  elif myMode == 'decrypt':
    translated = decryptMessage(myKey, myMessage)
  print('Using key %s' % (myKey))
  print('The %sed message is:' % (myMode))
  print(translated)
  
def checkValidKey(key):
  keyList = list(key)
  lettersList = list(LETTERS)
  keyList.sort()
  lettersList.sort()
  if keyList != lettersList:
      sys.exit('There is an error in the key or symbol set.')

def encryptMessage(key, message):
  return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
  return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
  translated = ''
  charsA = LETTERS
  charsB = key
  if mode == 'decrypt':
    # For decrypting, we can use the same code as encrypting. We
    # just need to swap where the key and LETTERS strings are used.
    charsA, charsB = charsB, charsA
    # loop through each symbol in the message
  print (message)
  for symbol in message:
    if symbol.upper() in charsA:
    # encrypt/decrypt the symbol
      symIndex = charsA.find(symbol.upper())
      if symbol.isupper():
        translated += charsB[symIndex].upper()
      else:
        translated += charsB[symIndex].lower()
        
    else:
      # symbol is not in LETTERS, just add it
      translated += symbol
  return translated


def getRandomKey():
  key = list(LETTERS)
  random.shuffle(key)
  return ''.join(key)


if __name__ == '__main__':
   main()   