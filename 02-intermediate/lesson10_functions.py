"""
LESSON 10: Functions
====================
Functions are reusable blocks of code that perform specific tasks.
"""

# DEFINING FUNCTIONS
# ------------------
print("=== DEFINING FUNCTIONS ===")

# Basic function
def greet():
    print("Hello, World!")

# Call the function
greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# RETURN VALUES
# -------------
print("\n=== RETURN VALUES ===")

# Function that returns a value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Multiple return values (using tuple)
def get_user_info():
    return "Alice", 25, "USA"

name, age, country = get_user_info()
print(f"Name: {name}, Age: {age}, Country: {country}")

# Early return
def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(f"4 is even: {is_even(4)}")
print(f"7 is even: {is_even(7)}")

# FUNCTION PARAMETERS
# -------------------
print("\n=== FUNCTION PARAMETERS ===")

# Default parameters
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

# Multiple parameters with defaults
def create_profile(name, age=18, city="Unknown"):
    return f"{name}, {age}, from {city}"

print(create_profile("Alice"))
print(create_profile("Bob", 25))
print(create_profile("Charlie", 30, "NYC"))

# Keyword arguments
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Buddy")
describe_pet(name="Whiskers", animal="cat")  # Order doesn't matter

# VARIABLE-LENGTH ARGUMENTS
# --------------------------
print("\n=== VARIABLE-LENGTH ARGUMENTS ===")

# *args - arbitrary number of positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum: {sum_all(1, 2, 3)}")
print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - arbitrary number of keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("\nUser info:")
print_info(name="Alice", age=25, city="NYC")

# Combining different parameter types
def complex_function(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function("Hello", 1, 2, 3, default="custom", key1="a", key2="b")

# DOCSTRINGS
# ----------
print("\n=== DOCSTRINGS ===")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

# Accessing docstrings with __doc__
# ----------------------------------
# What is __doc__?
# - Every function stores its docstring (the text in triple quotes) in an attribute called __doc__
# - You can access it using: function_name.__doc__
# - This is useful for getting documentation about what a function does

print("\n--- Reading a function's documentation ---")
print("The docstring says:")
print(calculate_area.__doc__)

# You can also use the help() function to see documentation
print("\nUsing help() function:")
help(calculate_area)

# Using the function normally
print(f"\nArea: {calculate_area(5, 3)}")

# Example: Why docstrings are helpful
# When working with someone else's code, you can check __doc__ to understand it
print("\n--- Checking other functions ---")
print("What does the 'len' function do?")
print(len.__doc__)

# SCOPE
# -----
print("\n=== SCOPE ===")

# Global variable
global_var = "I'm global"

def test_scope():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

test_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variables
count = 0

def increment():
    global count
    count += 1
    print(f"Count inside: {count}")

increment()
print(f"Count outside: {count}")

# LAMBDA FUNCTIONS
# ----------------
print("\n=== LAMBDA FUNCTIONS ===")

# Regular function
def square(x):
    return x ** 2

# Lambda (anonymous) function
square_lambda = lambda x: x ** 2

print(f"Square of 5: {square(5)}")
print(f"Square of 5 (lambda): {square_lambda(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"3 + 4 = {add(3, 4)}")

# Lambda in sorted()
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_people = sorted(people, key=lambda person: person["age"])
print(f"Sorted by age: {sorted_people}")

# Lambda in map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# Lambda in filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# HIGHER-ORDER FUNCTIONS
# -----------------------
print("\n=== HIGHER-ORDER FUNCTIONS ===")

# Function that takes another function as parameter
def apply_operation(numbers, operation):
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, double)
print(f"Doubled: {doubled}")

# Function that returns another function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_3 = create_multiplier(3)
times_5 = create_multiplier(5)

print(f"7 * 3 = {times_3(7)}")
print(f"7 * 5 = {times_5(7)}")

# RECURSION
# ---------
print("\n=== RECURSION ===")

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(7) = {fibonacci(7)}")

# Countdown
def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# DECORATORS (Preview)
# --------------------
print("\n=== DECORATORS (PREVIEW) ===")

# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# PRACTICAL EXAMPLES
# ------------------
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

# Example 2: Validate email
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

print(f"Valid: {is_valid_email('user@example.com')}")
print(f"Valid: {is_valid_email('invalid.email')}")

# Example 3: Calculate average
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

grades = [85, 92, 78, 90, 88]
print(f"Average grade: {calculate_average(grades):.2f}")

# Example 4: Find maximum
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

print(f"Max: {find_max([3, 7, 2, 9, 4])}")

# Example 5: Palindrome checker
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(f"'racecar' is palindrome: {is_palindrome('racecar')}")
print(f"'hello' is palindrome: {is_palindrome('hello')}")

# Example 6: Password validator
def is_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

print(f"'Pass123' strong: {is_strong_password('Pass123')}")
print(f"'weak' strong: {is_strong_password('weak')}")

# Example 7: Shopping cart
def calculate_total(items, tax_rate=0.08):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return {
        'subtotal': subtotal,
        'tax': tax,
        'total': total
    }

prices = [19.99, 29.99, 9.99]
result = calculate_total(prices)
print(f"Shopping cart: {result}")

# EXERCISES
# ----------
# 1. Write a function that returns the larger of two numbers
# 2. Create a function that calculates the area of a circle (πr²)
# 3. Write a function that checks if a number is prime
# 4. Create a function that reverses a string
# 5. Write a function that counts vowels in a string
# 6. Create a function that returns the nth Fibonacci number
# 7. Write a function that converts a list of Celsius temps to Fahrenheit
# 8. Create a calculator function with operations (+, -, *, /)
# 9. Write a function that finds all factors of a number
# 10. Create a function that generates a password with given length

# Write your solutions below:
