import pytest
from lib.count_words import *

"""
Enter an argument that is string
Expect it to return True
"""
def argument_is_string():
    result = count_words("Hair")
    assert result == True

"""
Enter an argument that is two words
Expect a return of a length of words in string 
"""
def argument_is_two_words():
    result = count_words("Hair of")
    assert result == 2


"""
Enter an argument that is not a string
Expect an error message
"""
def argument_is_not_a_string():
    with pytest.raises(Exception) as e:
        result = count_words(548)
    error_message = str(e.value)
    assert error_message == "Invalid entry, argument must be the string type."