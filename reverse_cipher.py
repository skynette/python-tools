'''
Reverse cipher encryption algorithm
'''


message = input("Message to be Encrypted: ")
translated = ''
i = len(message) - 1

mode = "encrypt"
print ("mode",mode)
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print("encrypted text >>>",translated)
