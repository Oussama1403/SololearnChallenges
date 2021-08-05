code = {"a":"z", "b":"y", "c":"x" ,"d":"w" ,"e":"v", "f":"u", "g":"t", "h":"s", "i":"r","j":"q","k":"p","l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d","x":"c", "y":"b", "z":"a"," ":" "}

plainText = input("Enter text to be encrypted: ")
plainText = plainText.lower() #Converts the input to lowecase letters for better management and error free program since python is case sensitive
encryptedText = ""
for c in plainText:
    if c in "abcdefghijklmnopqrstuvwxyz ":#checks if each character of plainText exist in 26 letters of alphabet
        encryptedText += code[c]
else: #if a character doesn't exist in the dictionary, do nothing to it
    #encryptedText+=c
    pass

print(encryptedText)
