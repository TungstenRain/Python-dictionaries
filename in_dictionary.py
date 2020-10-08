"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 11: Dictionaries in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
import time

def put_in_dictionary(a_list):
    """
        Take a list and put it in a dictionary

        a_list: list

        return: dictionary
    """
    a_dictionary = dict()
    for i in a_list:
        a_dictionary[i] = ''
    return a_dictionary


def make_word_list_append():
    """
        Reads lines from a file and builds a list using append

        return: list
    """
    # initialize variables
    a_list = []

    # open the file
    fin = open("words.txt")

    for line in fin:
        word = line.strip()
        a_list.append(word)
    
    # clsose the file
    fin.close()
    
    return a_list


if __name__ == '__main__':
    # initialize variables
    a_list = make_word_list_append()
    a_dictionary = dict()
    a_dictionary = put_in_dictionary(a_list)
    if 'hello' in a_dictionary:
        print("Success")