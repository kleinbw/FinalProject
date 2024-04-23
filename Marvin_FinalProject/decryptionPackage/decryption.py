# Name: Ben Klein, TJ Harrington, Ryan Wilkins
# email: kleinbw@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In the final project, we are in a group working together to decipher a code that will reveal a location on campus for us to find
# Brief Description of what this module does. This module contains the code for our decryption ran in the main module


import cryptography.fernet 
import json
from cryptography.fernet import Fernet

def readJSON(fileName):
        '''
        read from a text file into a python dictionary
        @parameter: file name is the file to read from
        '''
        
        return json.load(open(fileName))

def decryption(token):
    '''
    Input - A token that is required by fernet to decrypt the message
    Return - a fernet key that uses the token input
    '''
    f = Fernet('KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE=')
    return f.decrypt(token)
    

    