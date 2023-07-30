# sentence_grammar Function Design Recipe



## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and 
ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def sentence_grammar(sentence):
    """Verifies sentence begins with a capital and ends with a punctuation

    Parameters: (list all parameters and their types)
        sentence: containing a string that is a word (e.g. "hello")
        sentence: a string containing multiple words (e.g. "where is it")
        sentence: a string not beginning with a capital letter but ending with a punctuation (e.g. "hello world!")
        sentence: a string containing multiple words, begins with a capital and ends with a punctuation (e.g. "Where is it?")
        sentence: a string which begins with a number and ends with a punctuation (e.g. "3 blind mice ate cheese.")
        sentence: a string with a not beginning with but containing a capital letter in the middle of the sentence (e.g. "where is Sam?")

    Returns: (state the return value and its type)
        a string beginning with an uppercase letter or a number and ending with a punctuation mark (e.g. "Where is it?" or "3 blind mice ate cheese.")

        an error message:"Please capitalize the first letter in the sentence." and or "Please add a punctuation to the end of this sentence."


    Assumptions & Constraints:
        Sentence structure in terms of components aside from capitalisation of
        the first letter and punctuation at the end are not addressed.

    """

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence beginning with an capital letter
and ending with a punctuation
It returns a sentence beginning with an capital letter
and ending with a punctuation
"""
sentence_grammar("Where is it?") => "Where is it?"

"""
Given a sentence beginning with a number
and ending with a punctuation
It returns a sentence beginning with a number
and ending with a punctuation
"""
sentence_grammar "3 blind mice ate cheese." => "3 blind mice ate cheese."

"""
Given a string not beginning with a capital letter but ending with a punctuation
It returns a message requesting capitalization
"""
sentence_grammar("hello world!") => "Please capitalize the first letter in the sentence."

"""
Given a string containing multiple words
beginning with a capital letter and 
not ending with a punctuation
It returns messages asking for capitalization and punctuation
"""
sentence_grammar("Where is it") => "Please add a punctuation to the end of this sentence."

"""
Given a string containing multiple words
not beginning with a capital letter and 
not ending with a punctuation
It returns messages asking for capitalization and punctuation
"""
sentence_grammar("where is it") => "Please capitalize the first letter in the sentence."
"Please add a punctuation to the end of this sentence."

"""
Given a string that is a non-captialised word
It returns a error message 
"""
sentence_grammar("hello") => "Please capitalize the first letter in the sentence."
"Please add a punctuation to the end of this sentence."

"""
Given an empty string
It returns an empty list
"""
sentence_grammar("") => error_message: "No words entered, string is empty."



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.sentence_grammar import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_sentence_grammar_with_upper_then_lower():
    result = sentence_grammar("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

