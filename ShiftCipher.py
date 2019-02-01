import string


text_array=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#!-------------<String to value>----------!
def string_val(charecter):
  for i in range (len(text_array)):
    if (charecter == text_array[i]):
      return i
  

#!-------------<Value to String>----------!
def val_string(pos):
  return text_array[pos]

#!-------------<Import and Inputs>----------!

#!-------------<Encryption>----------!

def encrypt(text,key):
  encrypted_text=""
  print (encrypted_text)
  for i in text:
    
    if (i != " " and i != "."):
      
      encrypted_text = encrypted_text + val_string((string_val(str(i))+key)%26)
    else:
      encrypted_text = encrypted_text + i 
      
  return (encrypted_text) 

#!-------------<Decryption>----------!

def decrypt(text,key):
  decrypted_text=""
  print (decrypted_text)
  for i in text:
    
    if (i != " " and i != "."):
      
      decrypted_text = decrypted_text + val_string((string_val(str(i))-key)%26)
    else:
      decrypted_text = decrypted_text + i 
      
  return (decrypted_text) 
      


key=int(input("Enter Key : "))
text = (input("Enter text to encrypt : ")).lower()
encrypted_val = encrypt(text,key)
decrpted_text=decrypt(encrypted_val,key)
print ("Encrypted: "+encrypted_val)
print ("Decrypted: "+ decrpted_text)

#!-------------<CryptoAnalysis (Breaking the encryption) >----------!
#for 26 charecter or alphabets only

def find_key():
  for i in range(0,26):
    decrypt(encrypted_val,i)
    