import pytest
from lib.sentence_grammar import *

"""
Given a sentence beginning with an capital letter
and ending with a punctuation
It returns a sentence beginning with an capital letter
and ending with a punctuation
"""
def test_verified_grammar_sentence():
    result = sentence_grammar("Where is it?")
    assert result == "Where is it?" 

"""
Given a sentence beginning with a number
and ending with a punctuation
It returns a sentence beginning with a number
and ending with a punctuation
"""
def test_begin_with_number_end_with_punctuation():
    result = sentence_grammar("3 blind mice ate cheese.")
    assert result == "3 blind mice ate cheese."

"""
Given a string not beginning with a capital letter but ending with a punctuation
It returns a message requesting capitalization
"""
def test_no_capital_yes_punctuation():
    result = sentence_grammar("hello world!")
    assert result == "Please capitalize the first letter in the sentence."

"""
Given a string containing multiple words
not beginning with a capital letter and 
not ending with a punctuation
It returns messages asking for capitalization and punctuation
"""
def test_capital_but_no_punctuation():
    result = sentence_grammar("Where is it")
    assert result == "Please add a punctuation to the end of this sentence."

"""
Given a string containing multiple words
not beginning with a capital letter and 
not ending with a punctuation
It returns messages asking for capitalization and punctuation
"""
def test_multiple_words_no_capital_and_no_punctuation():
    result = sentence_grammar("where is it")
    assert result == "Please capitalize the first letter in the sentence and add a punctuation to the end of this sentence."

"""
Given a string that is a non-captialised word
It returns a error message 
"""
def test_single_word_no_capital_and_no_punctuation():
    result = sentence_grammar("hello")
    assert result == "Please capitalize the first letter in the sentence and add a punctuation to the end of this sentence."

"""
Given an empty string
It returns an empty list
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        result = sentence_grammar("")
    error_message = str(e.value)
    assert error_message == "No words entered, string is empty."
