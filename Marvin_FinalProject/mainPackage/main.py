'''
Created on Apr 10, 2024

@author: kleinbw
'''

from decryptionPackage.decryption import *
from txtPackage.txt import *


Data = readJSON("EncryptedGroupHints Spring 2024 Section 002.json")
Marvin = Data["Marvin"]
print(Marvin)
#Creating a DF For the words 
words = read_words_from_file("UCEnglish.txt")


#CREATING LOOP WILL LIKELY BE ABLE TO BE FUNCTIOn
values = []
for x in Marvin:
    y = int(x)
    values.append(words[y])
print(values)

#EXTRACTING RAW ENCRYPTION DATA
Encrypted = readJSON("TeamsAndEncryptedMessagesForDistribution - 002.json")
Encrypted = Encrypted["Marvin"]
print(Encrypted)
    