"""
A function called make_snippet 
that takes a string as an argument
and returns the first five words
- if there are more than five words 
then adds '...' 
after the first five words
"""
def make_snippet(words):
    if words == "":
        return "Please enter words."
    elif len(words.split()) <= 5:
        return words
    else: 
        # split string to list of five words
        # join the list of words
        # concatenate the '...' to the string 
        split_words_first_five = words.split()[:5]
        sentence = " ".join(split_words_first_five)
        append_sentence = sentence + " ..."
        return append_sentence


