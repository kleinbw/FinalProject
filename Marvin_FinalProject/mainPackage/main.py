# Name: Ben Klein, TJ Harrington, Ryan Wilkins
# email: kleinbw@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In the final project, we are in a group working together to decipher a code that will reveal a location on campus for us to find
# Brief Description of what this module does. This is the main module and in here all of our code runs. this is where we determine what the decryption is 
# Citations: None

from decryptionPackage.decryption import *
from functionsPackage.functions import *
from txtPackage.txt import *
from PIL import Image

if __name__ == "__main__":
    Data = readJSON("EncryptedGroupHints Spring 2024 Section 002.json")
    Marvin = Data["Marvin"]
    words = read_words_from_file("UCEnglish.txt")
    print(decrypt_Marvin(Marvin, words))

    #EXTRACTING RAW ENCRYPTION DATA
    Encrypted = readJSON("TeamsAndEncryptedMessagesForDistribution - 002.json")
    Encrypted = Encrypted["Marvin"]
    Encrypted = str(Encrypted)
    
    print(decryption(Encrypted))   
    myimage = load_image(("FinalPhoto.jpeg"))
    myimage.show()
