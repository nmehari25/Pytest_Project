class GrammarStats:
    def __init__(self):
        # check a number of texts meet the definition
        # of a sentence and then texts that have
        # passed tests
        self._sentences = 0
        self._passed = 0 

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        # Empty string
        self._sentences += 1
        if text == "" or text == None:
            raise Exception ("Please enter a sentence.")
        elif (text[0].isupper() or text[0].isdigit()) and text.endswith((".", "!", "?")):
            self._passed += 1
            return True
        else:
            return False


    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self._sentences == 0:
            return 0
        else:
            return round((self._passed / self._sentences) * 100)
        
