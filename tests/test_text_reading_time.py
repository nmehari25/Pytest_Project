import pytest
from lib.text_reading_time import *

"""
Given a string containing only a word
It returns 3.33 seconds
"""

def test_string_containing_only_a_word():
    result = text_reading_time("Really")
    assert result == 3.33

"""
Given a string containing only five words
It returns 16.65 seconds
"""
def test_string_containing_only_five_words():
    result = text_reading_time("Hey Sam how are you")
    assert result == 16.65

"""
Given a string containing words and punctuations
It returns the 3.33 seconds per word in the string
"""
def test_string_containing_only_five_words():
    result = text_reading_time("Hey Sam, How are you?")
    assert result == 16.65

"""
Given a string containing words and emojis
It returns the 3.33 seconds per word and emoji
"""
def test_string_containing_words_and_emojis():
    result = text_reading_time("Hey 🙂 Sam 👋🏾")
    assert result == 13.32

"""
Given a string containing words and numbers
It returns the 3.33 seconds per word and number
"""
def test_string_containing_words_and_emojis():
    result = text_reading_time("He is number 10 in the league")
    assert result == 23.31

"""
Given a string containing an empty string
It returns a error message informing that the text is empty
"""
def test_string_containing_an_empty_string():
    with pytest.raises(Exception) as e:
        result = text_reading_time("")
    error_message = str(e.value)
    assert error_message == "This is an empty text"
