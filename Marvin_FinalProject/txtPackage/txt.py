


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

