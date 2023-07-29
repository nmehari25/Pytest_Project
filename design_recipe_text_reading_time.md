# text_reading_time Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute.

calculation of time per amount of words read:
(200 words/minute)/(60 seconds/minute) = 3.33 words/second

* any words that are 3 words or less are estimated up
to take a second of reading time

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def text_reading_time(text_message):
    """Estimates the reading time of a text

    Parameters: (list all parameters and their types)
        text_message: a string containing only a word (e.g. "Really")
        text_message: a string containing only five words (e.g. "Hey Sam how are you")
        text_message: a string containing words and punctuations (e.g. "Hey Sam, How are you?")
        text_message: a string containing words and emojis (e.g. "Hey 🙂 Sam 👋🏾")
        text_message: a string containing words and numbers (e.g. "He is number 10 in the league")
        text_message: an empty string (e.g. "")
        text_message: a None value

    Returns: (state the return value and its type)
        a string with one word ("Really")
        a string with five words (e.g. "Hey Sam how are you")
        a string with punctuations and words (e.g. "Hey Sam, How are you?")
        a string with words and emojis (e.g. "Hey 🙂 Sam 👋🏾")
        a string containing words and numbers (e.g. "He is number 10 in the league")
        an error message in string format: "This is an empty text"



    Side effects: (state any side effects)
        The assumption is made that any characters other than letters in the
        alphabet are considered part of a word if they are appended to it or a word if it stands alone with a space on either side (e.g. " :) " or " 👍🏾 " or " Bye😊 " or "10")
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests


```python
# EXAMPLE

"""
Given a string containing only a word
It returns 3.33 seconds
"""
text_reading_time("Really") => 3.33

"""
Given a string containing only five words
It returns 16.65 seconds
"""
text_reading_time("Hey Sam how are you") => 16.65

"""
Given a string containing words and punctuations
It returns the 3.33 seconds per word in the string
"""
text_reading_time("Hey Sam, How are you?") => 16.65

"""
Given a string containing words and emojis
It returns the 3.33 seconds per word and emoji
"""
text_reading_time("Hey 🙂 Sam 👋🏾") => 13.32

"""
Given a string containing words and numbers
It returns the 3.33 seconds per word and number
"""
text_reading_time("He is number 10 in the league") => 23.31

"""
Given a string containing an empty string
It returns a error message informing that the text is empty
"""
text_reading_time("") => "This is an empty text"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

