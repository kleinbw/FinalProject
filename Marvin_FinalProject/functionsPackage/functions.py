#functions.py

# Name: Ben Klein, TJ Harrington, Ryan Wilkins
# email: kleinbw@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In the final project, we are in a group working together to decipher a code that will reveal a location on campus for us to find
# Brief Description of what this module does. The Functions module contains all of the functions we wrote for the final project. 
# Citations: None


from PIL import Image
from decryptionPackage.decryption import *
from txtPackage.txt import *
def decrypt_Marvin(data, words):
   decrypted_values = []
   for x in data:
       y = int(x)
       decrypted_values.append(words[y])
   return decrypted_values
   Data = readJSON("EncryptedGroupHints Spring 2024 Section 002.json")
   Marvin = Data["Marvin"]
   print(Marvin) #Can be deleted

#Creating a DF For the words 

   words = read_words_from_file("UCEnglish.txt")
   decrypted_values = decrypt_Marvin(Marvin, words)
   print(decrypted_values)

def load_image( filename ) :

   '''
   Load an image file from disk
   @param: filename The file to load
   @return: the image object or none if an error occurred 
   '''

#This is 'test' code for this module 

   myimage = Image.open(filename)    
   myimage.load()
   return myimage

