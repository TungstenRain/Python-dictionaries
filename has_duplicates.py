"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 11: Dictionaries in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def has_duplicates(a_sequence):
    """
        Determine if any element appears more than once in a sequence.
        Simple version using a for loop.
        
        t: sequence

        return: boolean; True if has more than one element in a sequence, false otherwise
    """
    a_dictionary = {}
    for x in a_sequence:
        if x in a_dictionary:
            return True
        a_dictionary[x] = True
    return False


def has_duplicates2(a_sequence):
    """
        Determine if any element appears more than once in a sequence.
        Faster version using a set.
        
        t: sequence

        return: boolean; True if element appears more than once in a sequence, false otherwise
    """
    return len(set(a_sequence)) < len(a_sequence)


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))