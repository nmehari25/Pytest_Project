import pytest
from lib.make_snippet import *

"""
A function called make_snippet 
that takes a string as an argument
and returns the first five words
- if there are more than that 
and then adds '...' 
after the first five words
"""

"""
If no words has been entered
Expect a message to please enter a words.
"""
def test_no_string_is_entered():
    result = make_snippet("")
    assert result == "Please enter words."
    
"""
If string has five words
Expect the five words to be returned
"""
def test_argument_is_five_words():
    result = make_snippet("The quick brown fox jumped")
    assert result == "The quick brown fox jumped"

"""
If string has more than five words
Expect the first five words to be printed
followed by '...'
"""
def test_argument_is_more_than_five_words():
    result = make_snippet("The quick brown fox jumped over the lazy dog.")
    assert result == "The quick brown fox jumped ..." 