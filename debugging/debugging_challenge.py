
"""First Exercise"""

# def say_hello(name):
#     return "hello {name}"

# # Intended output:
# #
# # > say_hello("kay")
# # => "hello kay"

# Answer 1
"""
To print the statement with a argument in it
needs to be formatted as a string
"""
# def say_hello(name):
#     return f'hello {name}'

# Answer 2
# class Person: 
#     def __init__(self, name):
#     self.name = name
#         def greeting(self):
#         return f'hi, my name is {self.name}'


"""Cipher Exercise 2"""
# def encode(text, key):
#     cipher = make_cipher(key)

#     ciphertext_chars = []
#     for i in text:
#         ciphered_char = chr(65 + cipher.index(i))
#         ciphertext_chars.append(ciphered_char)

#     return "".join(ciphertext_chars)


# def decode(encrypted, key):
#     cipher = make_cipher(key)

#     plaintext_chars = []
#     for i in encrypted:
#         plain_char = cipher[65 - ord(i)]
#         plaintext_chars.append(plain_char)

#     return "".join(plaintext_chars)


# def make_cipher(key):
#     alphabet = [chr(i + 98) for i in range(1, 26)]
#     cipher_with_duplicates = list(key) + alphabet

#     cipher = []
#     for i in range(0, len(cipher_with_duplicates)):
#         if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
#             cipher.append(cipher_with_duplicates[i])

#     return cipher

# # When you run this file, these next lines will show you the expected
# # and actual outputs of the functions above.
# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)



""" Answer to Cipher Exercise 2 """

# def encode(text, key):
#     cipher = make_cipher(key)

#     ciphertext_chars = []
#     for i in text:
"""
Letter turned into another letter a number of positions
further down and 65 letters added to it,
then used unicode to return a new letter which 
corresponds to the unicode
"""
#         ciphered_char = chr(65 + cipher.index(i))
#         ciphertext_chars.append(ciphered_char)

#     return "".join(ciphertext_chars)


# def decode(encrypted, key):
#     cipher = make_cipher(key)

#     plaintext_chars = []
#     for i in encrypted:
"""
Error 1: to decode you need to subtract the 65 characters
down the alphabet which you added to the letter before the
string representing unicode character at that position
was returned with the chr() method for the encryption above
"""
#         plain_char = cipher[ord(i) - 65]
#         plaintext_chars.append(plain_char)

#     return "".join(plaintext_chars)


# def make_cipher(key):
"""
Error 2: chr() method returns a string character corresponding to
unicode integer. 
- There are 26 letters in the alphabet and 
therefore the range (1, 26) only covers 25 of them. 
So, we begin the range with 0. 
- Also, 98 is the letter B in unicode and 97 is A. 
We want to begin deciphering with the first letter
in the alphabet as we go through it.
"""
#     alphabet = [chr(i + 97) for i in range(0, 26)]
#     cipher_with_duplicates = list(key) + alphabet
#     # print(f'{cipher_with_duplicates}')

#     cipher = []
#     for i in range(0, len(cipher_with_duplicates)):
#         if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
#             cipher.append(cipher_with_duplicates[i])

#     return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#       {make_cipher('nebiat')}

# """)
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
# Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}


"""
Exercise: Using print to get visibility
"""
# def factorial(n):
#     product = 1
#     print(f"at the start product is {product}")
#     while n > 0:
#         n -= 1
#         print(f"we multiply {product} by {n}")
#         product *= n
#         print(f"we get {product}")

#         return product
# print(f"""
#  Running: factorial(5)
# Expected: 120
#   Actual: {factorial(5)}
# """)

"""
Answer for: Using print to get visibility
"""
# def factorial(n):
#     product = 1
#     print(f"at the start product is {product}")
#     while n > 0:
#         """ 
#         the product should be multiplied before decrementing 
#         the factorial
#         """
#         product *= n
#         print(f"we get {product}")
#         n -= 1
#         print(f"we multiply {product} by {n}")
#     """
#     we want to return the product after the loop runs until
#     the while statement is no longer TRUE and then 
#     the final product to be the output
#     """
#     return product

# print(f"""
# Running: factorial(5)
# Expected: 120
# Actual: {factorial(5)}
# """)

"""Challenge"""
def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")


# Answer for Challenge
def get_most_common_letter(text):
    # Initialize an empty dictionary to keep track of character counts
    text_no_space = text.replace(" ","")
    print(text_no_space)
    counter = {}
    # Iterate over each character in the text
    for char in text_no_space:
        # Update the count of the character in the dictionary
        # If the character is not already a key, set its count to 0 and add 1
        # If the character is already a key, increment its count by 1
        counter[char] = counter.get(char, 0) + 1
        
    
    # Sort the items in the counter dictionary based on their values (counts)
    # Get the first item (character and count) in the sorted list
    # Extract the count from the item and assign it to the variable 'letter'
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    
    print(f"Counter dictionary: {counter}")  # Print the counter dictionary
    print(f"Letter count: {letter}")  # Print the count of the most common letter
    
    # Return the most common letter count
    return letter


# Print a formatted string showing the expected and actual results
print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!")
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

