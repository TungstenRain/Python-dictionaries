"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 11: Dictionaries in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def rotate_letter(letter, amount):
    """
        Apply a simple Caesar Cypher by rotating each letter in a word by a user-specified amount

        word: string to rotate
        amount: integer, amount to rotate each letter

        return: a single-letter string rotated
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    
    c = ord(letter) - start
    i = (c + amount) % 26 + start
    return chr(i)


def rotate_word(word, amount):
    """
        Apply a simple Caesar Cypher by rotating each letter in a word by a user-specified amount

        word: string to rotate
        amount: integer, amount to rotate each letter

        return: string rotated
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, amount)
    return res


def make_word_dict():
    """
        Read the words in 'words.txt' and return a dictionary that contains the words as keys

        return: dictionary
    """
    # initialize variables
    a_dictionary = dict()

    # open the file
    fin = open('words.txt')

    for line in fin:
        word = line.strip().lower()
        a_dictionary[word] = None

    # close the file
    fin.close()

    return a_dictionary


def rotate_pairs(word, word_dict):
    """
        Prints all words that can be generated by rotating word.
    
        word: string
        word_dict: dictionary with words as keys
    """
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


if __name__ == '__main__':
    word_dict = make_word_dict()

    for word in word_dict:
        rotate_pairs(word, word_dict)