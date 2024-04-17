# Name: Ben Klein, TJ Harrington, Ryan Wilkins
# email: kleinbw@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In the final project, we are in a group working together to decipher a code that will reveal a location on campus for us to find
# Brief Description of what this module does. This module contains the code reads the text file in for UCEnglish.txt


def read_words_from_file(file_path):
    '''
    Read words from a text file with one word per line and return a list
    
    Parameters:
    -File_parth (str):The path to the text file.
    
    Returns:
    -List: A list containing words from a file
    '''
    with open(file_path, 'r') as file:
        # Read lines from the file and remove leading/trailing whitespaces
        words = [line.strip() for line in file.readlines()]
    return words

