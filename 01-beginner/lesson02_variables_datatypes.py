"""
LESSON 2: Variables and Data Types
===================================
Variables store data. Python is dynamically typed, 
so you don't need to declare variable types.
"""

# VARIABLES
# Variable names should be descriptive
name = "Noah"
age = 25
height = 5.9
is_student = True
Name="Noah" # This is not recommended as it's the same as the first variable name
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# VARIABLE NAMING RULES
# - Must start with a letter or underscore
# - Can contain letters, numbers, and underscores
# - Case-sensitive (age and Age are different)
# - Cannot use Python keywords (if, for, while, etc.)

# Good variable names
user_name = "John"
total_price = 99.99
item_count = 5

# BASIC DATA TYPES
# ----------------

# 1. INTEGER (int) - whole numbers
number = 42
negative_number = -17
print("\nInteger:", number, type(number))
print("\nInteger:", number, type(number))

# 2. FLOAT (float) - decimal numbers
price = 19.99
temperature = -5.5
print("Float:", price, type(price))

# 3. STRING (str) - text
message = "Hello, Python!"
single_quotes = 'This "you\'re" too'
print("String:", message, type(message))
print(single_quotes)

# 4. BOOLEAN (bool) - True or False
is_raining = False
is_sunny = True
print("Boolean:", is_sunny, type(is_sunny))

# TYPE CONVERSION
# ---------------
# Converting between data types

# String to integer
age_text = "30"
age_number = int(age_text)
print("\nConverted to int:", age_number, type(age_number))

# Integer to string
count = 100
count_text = str(count)
print("Converted to string:", count_text, type(count_text))

# String to float
price_text = "49.99"
price_number = float(price_text)
print("Converted to float:", price_number, type(price_number))

# Integer to float
whole_number = 10
decimal_number = float(whole_number)
print("Converted to float:", decimal_number)

# CHECKING TYPES
# Use type() function to check data type
print("\nType checking:")
print("Type of 42:", type(42))
print("Type of 3.14:", type(3.14))
print("Type of 'Hello':", type("Hello"))
print("Type of True:", type(True))

# EXERCISES
# ----------
# 1. Create variables for your first name, last name, and full name
# 2. Create a variable for your birth year and calculate your age
# 3. Create a variable for your height in feet (float) and weight in pounds (int)
# 4. Convert a string "123" to an integer and multiply it by 2
# 5. Create a boolean variable indicating if you like pizza

# Write your solutions below:
