"""
A function called count_words that 
takes a string as an argument and 
returns the number of words in that string.
"""

def count_words(words):
    if words is isinstance(words, str):
        # split string into list > string.split()
        # find number of words in list > len(list)
        length_words = len(words.split())
        return length_words
    else:
        raise Exception("Invalid entry, argument must be the string type.")
        





