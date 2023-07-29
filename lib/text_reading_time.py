def text_reading_time(words):
    if words == "":
        raise Exception("This is an empty text")
    else:
        # Count the number of 'words' in the string
        # > split words into list str.split()
        # > use len(list) to count the number of 'words'
        # > multiply the number of words by 3.33 seconds/word
        # > round the number of seconds to two decimal places
        split_words = words.split()
        number_words = len(split_words)
        reading_time = round((number_words * 3.33),2)
        return reading_time

