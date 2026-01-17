"""
LESSON 4: Strings
=================
Strings are sequences of characters used to store text.
"""

# CREATING STRINGS
# ----------------
print("=== CREATING STRINGS ===")

single_quotes = 'Hello'
double_quotes = "World"
multi_line = """This is a
multi-line
string"""

print(single_quotes)
print(double_quotes)
print(multi_line)

# STRING INDEXING
# ---------------
print("\n=== STRING INDEXING ===")
# Strings are indexed starting from 0

text = "Python"
print(f"Text: {text}")
print(f"First character (index 0): {text[0]}")
print(f"Third character (index 2): {text[2]}")
print(f"Last character (index -1): {text[-1]}")
print(f"Second to last (index -2): {text[-2]}")

# STRING SLICING
# --------------
print("\n=== STRING SLICING ===")
# Syntax: string[start:end:step]

message = "Hello, World!"
print(f"Message: {message}")
print(f"Characters 0-5: {message[0:5]}")  # Hello
print(f"Characters 7-12: {message[7:12]}")  # World
print(f"From start to index 5: {message[:5]}")  # Hello
print(f"From index 7 to end: {message[7:]}")  # World!
print(f"Every 2nd character: {message[::2]}")  # Hlo ol!
print(f"Reverse string: {message[::-1]}")  # !dlroW ,olleH

# STRING METHODS
# --------------
print("\n=== STRING METHODS ===")

sample = "  Python Programming  "
print(f"Original: '{sample}'")

# Case conversion
print(f"Upper: {sample.upper()}")
print(f"Lower: {sample.lower()}")
print(f"Title: {sample.title()}")
print(f"Capitalize: {sample.capitalize()}")

# Whitespace removal
print(f"Strip: '{sample.strip()}'")
print(f"Left strip: '{sample.lstrip()}'")
print(f"Right strip: '{sample.rstrip()}'")

# Search and replace
text = "I love Python. Python is great!"
print(f"\nText: {text}")
print(f"Count 'Python': {text.count('Python')}")
print(f"Find 'Python': {text.find('Python')}")  # Returns index
print(f"Replace: {text.replace('Python', 'Java')}")

# Check string properties
word = "Hello"
print(f"\nWord: {word}")
print(f"Is alphabetic: {word.isalpha()}")
print(f"Is numeric: {word.isdigit()}")
print(f"Is alphanumeric: {word.isalnum()}")
print(f"Starts with 'He': {word.startswith('He')}")
print(f"Ends with 'lo': {word.endswith('lo')}")

# STRING CONCATENATION
# --------------------
print("\n=== STRING CONCATENATION ===")

first_name = "John"
last_name = "Doe"

# Using + operator
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Using join()
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"Joined: {sentence}")

# STRING FORMATTING
# -----------------
print("\n=== STRING FORMATTING ===")

name = "Alice"
age = 30
height = 5.6

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
print(f"My name is {name}, I am {age} years old.")
print(f"Height: {height:.1f} feet")  # Format to 1 decimal place

# Method 2: format() method
print("My name is {}, I am {} years old.".format(name, age))
print("My name is {n}, I am {a} years old.".format(n=name, a=age))

# Method 3: % operator (old style)
print("My name is %s, I am %d years old." % (name, age))

# Advanced formatting
price = 49.99567
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Price: ${price:>10.2f}")  # Right-aligned, width 10

number = 42
print(f"Binary: {number:b}")
print(f"Hex: {number:x}")
print(f"Octal: {number:o}")

# STRING ESCAPE CHARACTERS
# ------------------------
print("\n=== ESCAPE CHARACTERS ===")

print("Line 1\nLine 2")  # \n = newline
print("Tab\there")  # \t = tab
print("Quote: \"Hello\"")  # \" = quote
print("Backslash: \\")  # \\ = backslash
print('It\'s a nice day')  # \' = single quote

# Raw strings (ignore escape characters)
path = r"C:\Users\Noah\Documents"
print(f"Path: {path}")

# STRING LENGTH
# -------------
print("\n=== STRING LENGTH ===")

text = "Python Programming"
print(f"Text: {text}")
print(f"Length: {len(text)}")

# EXERCISES
# ----------
# 1. Create a string with your full name and print each word on a separate line
# 2. Take a sentence and print it in reverse
# 3. Create a string "hello world" and convert it to "Hello World"
# 4. Count how many times the letter 'a' appears in "banana"
# 5. Create variables for first name, last name, and age, then use an f-string 
#    to print: "My name is [first] [last] and I am [age] years old."
# 6. Extract the word "Python" from the string "I love Python programming"

# Write your solutions below:
