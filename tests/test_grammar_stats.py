import pytest
from lib.grammar_stats import GrammarStats

"""
Given an empty text
an error message is received
"""
def test_text_is_empty_string():

    with pytest.raises(Exception) as e:
        _sentence = GrammarStats() 
        _sentence.check("")
    assert str(e.value) == "Please enter a sentence."

"""
Given a string with a capitalised first letter
or a number at the beginning
and a punctuation mark at the end
The result is 'True'
"""
def test_first_letter_is_captialised_and_ends_with_punctuation():
    _sentence = GrammarStats()
    result = _sentence.check("Why does this take so long?")
    assert result == True

"""
Given text does not pass the
sentence check
The result is 'False'
"""
def test_text_does_not_pass():
    _sentence = GrammarStats()
    result = _sentence.check("Why does this take so long")
    assert result == False

"""
Given the no sentences were checked
there _percentage_good is 0
"""
def test_no_sentences_were_checked():
    _sentence = GrammarStats()
    result = _sentence.percentage_good()
    assert result == 0

"""
Given the 5 sentences were checked
and passed
the _percentage_good is 100
"""
def test_5_sentences_were_checked_and_all_passed():
    _passed = GrammarStats()
    assert _passed.check("This is a sentence.") == True
    assert _passed.check("Another sentence.") == True
    assert _passed.check("One more sentence.") == True
    assert _passed.check("Definitely a good one.") == True
    assert _passed.check("Final excellent one.") == True
    result = _passed.percentage_good()
    assert result == 100

"""
Given the 4 sentences were checked
and 1 passed
the _percentage_good is 75
"""
def test_4_sentences_were_checked_and_1_passed():
    _passed = GrammarStats()
    assert _passed.check("This is a sentence.") == True
    assert _passed.check("Another sentence.") == True
    assert _passed.check("One more sentence.") == True
    assert _passed.check("Not a good one") == False
    result = _passed.percentage_good()
    assert result == 75