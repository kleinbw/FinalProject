'''
Created on Apr 10, 2024

@author: kleinbw
'''
#import cryptography.fernet as crypt
import json

def readJSON(fileName):
        '''
        read from a text file into a python dictionary
        @parameter: file name is the file to read from
        '''
        
        return json.load(open(fileName))

#def decryption():
    