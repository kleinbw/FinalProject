'''
Created on Apr 10, 2024

@author: kleinbw
'''
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
    f = Fernet('KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE=')
    return f.decrypt(token)
    

    