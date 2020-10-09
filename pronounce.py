"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 11: Dictionaries in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def read_dictionary(filename='c06d'):
    """
        Reads from a file and builds a dictionary that maps from each word 
        to a string that describes its primary pronunciation.
        Secondary pronunciations are added to the dictionary with a number, 
        in parentheses, at the end of the key, so the key for the second pronunciation of "abdominal" is "abdominal(2)".
        
        filename: string
        
        return: map from string to pronunciation
    """
    # initialize variables
    a_dictionary = dict()

    # open the file
    fin = open(filename)
    
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        a_dictionary[word] = pron

    # close the file
    fin.close()

    return a_dictionary


def make_word_dict():
    """
        Read the words in words.txt and return a dictionary that contains the words as keys.

        return: dictionary
    """
    # initialize variables
    a_dictionary = dict()

    # open the file
    fin = open('words.txt')

    for line in fin:
        word = line.strip().lower()
        a_dictionary[word] = word
    
    # close the file
    fin.close()

    return a_dictionary


def homophones(word_a, word_b, phonetic_map):
    """
        Determines if two words can be pronounced the same way. 
        word_a: string
        word_b: string
        phonetic_map: map from words to pronunciation codes

        return: boolean; True if words can be pronounced the same way, false otherwise
    """
    if word_a not in phonetic_map or word_b not in phonetic_map:
        return False

    return phonetic_map[word_a] == phonetic_map[word_b]


def check_word(word, word_dictionary, phonetic_map):
    """
        Determine if the word has the following property:
            removing the first letter yields a word with the same pronunciation, and removing the second letter yields a word with the same pronunciation.
        
        word: string
        word_dict: dictionary with words as keys
        phonetic: map from words to pronunciation codes

        return: boolean; True if word has the properties, false otherwise
    """
    word_1 = word[1:] 
    if word_1 not in word_dictionary:
        return False
    if not homophones(word, word_1, phonetic_map):
        return False

    word_2 = word[0] + word[2:]
    if word_2 not in word_dictionary:
        return False
    if not homophones(word, word_2, phonetic_map):
        return False

    return True


if __name__ == '__main__':
    phonetic = read_dictionary()
    word_dict = make_word_dict()

    for word in word_dict:
        if check_word(word, word_dict, phonetic):
            print(word, word[1:], word[0] + word[2:])