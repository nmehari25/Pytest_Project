def sentence_grammar(sentence):
    if sentence == (""):
        raise Exception("No words entered, string is empty.")
    if (sentence[0].isupper() or sentence[0].isdigit()) and sentence.endswith((".", "!", "?")):
        return sentence
    elif sentence[0].islower() and sentence.endswith((".", "!", "?")):
        return "Please capitalize the first letter in the sentence."
    elif (sentence[0].isupper() or sentence[0].isdigit()) and not sentence.endswith((".", "!", "?")):
        return "Please add a punctuation to the end of this sentence."
    else:
        not(sentence[0].isupper() or sentence[0].isdigit()) and not sentence.endswith((".", "!", "?"))
        return "Please capitalize the first letter in the sentence and add a punctuation to the end of this sentence."
    
