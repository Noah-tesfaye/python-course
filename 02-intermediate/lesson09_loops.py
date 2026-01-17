"""
LESSON 9: Loops
===============
Loops allow you to repeat code multiple times.
"""

# FOR LOOPS
# =========

# BASIC FOR LOOP
# --------------
print("=== BASIC FOR LOOP ===")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through a string
for char in "Python":
    print(char)

# RANGE FUNCTION
# --------------
print("\n=== RANGE FUNCTION ===")

# range(stop) - from 0 to stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop) - from start to stop-1
print("range(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step)
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Reverse range
print("range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# ENUMERATE
# ---------
print("\n=== ENUMERATE ===")

# Get both index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Start enumeration from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")

# ZIP FUNCTION
# ------------
print("\n=== ZIP FUNCTION ===")

# Iterate over multiple lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# LOOP WITH DICTIONARIES
# ----------------------
print("\n=== LOOP WITH DICTIONARIES ===")

student = {"name": "Alice", "age": 20, "grade": 95}

# Loop through keys
for key in student:
    print(f"{key}: {student[key]}")

# Loop through items
for key, value in student.items():
    print(f"{key} = {value}")

# WHILE LOOPS
# ===========

# BASIC WHILE LOOP
# ----------------
print("\n=== BASIC WHILE LOOP ===")

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# WHILE WITH CONDITION
# --------------------
print("\n=== WHILE WITH CONDITION ===")

number = 1
while number <= 10:
    print(number, end=" ")
    number += 1
print()

# User input loop (commented to avoid blocking)
# password = ""
# while password != "python":
#     password = input("Enter password: ")
# print("Access granted!")

# BREAK STATEMENT
# ---------------
print("\n=== BREAK STATEMENT ===")

# Exit loop early
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print()

# Find first even number
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

# CONTINUE STATEMENT
# ------------------
print("\n=== CONTINUE STATEMENT ===")

# Skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print()

# Skip negative numbers
numbers = [-2, -1, 0, 1, 2, 3]
for num in numbers:
    if num < 0:
        continue
    print(num, end=" ")
print()

# ELSE CLAUSE IN LOOPS
# --------------------
print("\n=== ELSE CLAUSE ===")

# else executes when loop completes normally (no break)
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed!")

# else doesn't execute if break is used
for i in range(5):
    if i == 3:
        print(f"\nBreaking at {i}")
        break
    print(i, end=" ")
else:
    print("This won't print")

# NESTED LOOPS
# ------------
print("\n=== NESTED LOOPS ===")

# Multiplication table
print("Multiplication Table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

# Pattern printing
print("\nPattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# LOOP CONTROL PATTERNS
# ---------------------
print("\n=== LOOP CONTROL PATTERNS ===")

# Pattern 1: Loop until condition
count = 0
while True:
    print(f"Count: {count}")
    count += 1
    if count >= 3:
        break

# Pattern 2: Skip and continue
for i in range(10):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    print(i, end=" ")
print()

# LIST COMPREHENSION (Alternative to loops)
# ------------------------------------------
print("\n=== LIST COMPREHENSION ===")

# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(f"Traditional: {squares}")

# List comprehension (more Pythonic)
squares = [x**2 for x in range(1, 6)]
print(f"Comprehension: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# PRACTICAL EXAMPLES
# ------------------
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Sum of numbers
total = 0
for i in range(1, 11):
    total += i
print(f"Sum 1-10: {total}")

# Example 2: Find all even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# Example 3: Reverse a string
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Reversed: {reversed_text}")

# Example 4: Count vowels
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Vowel count: {count}")

# Example 5: Factorial
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Example 6: Fibonacci sequence
n = 10
a, b = 0, 1
print(f"First {n} Fibonacci numbers:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Example 7: Prime number checker
num = 17
is_prime = True
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False
print(f"{num} is prime: {is_prime}")

# Example 8: Search in list
shopping_list = ["milk", "eggs", "bread", "butter"]
item = "eggs"
found = False
for i, product in enumerate(shopping_list):
    if product == item:
        print(f"Found {item} at index {i}")
        found = True
        break
if not found:
    print(f"{item} not in list")

# Example 9: Matrix traversal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Example 10: Menu system
menu = """
1. Option 1
2. Option 2
3. Exit
"""
choice = 0
while choice != 3:
    print(menu)
    # In real code: choice = int(input("Choose: "))
    # For demo:
    print("Selecting option 3 to exit")
    choice = 3

# EXERCISES
# ----------
# 1. Print numbers from 1 to 50
# 2. Calculate the sum of all numbers from 1 to 100
# 3. Print all even numbers between 1 and 20
# 4. Create a list of squares of numbers from 1 to 10
# 5. Count how many times a letter appears in a string
# 6. Find the largest number in a list using a loop
# 7. Print a multiplication table for numbers 1-10
# 8. Reverse a list without using reverse() method
# 9. Check if a word is a palindrome
# 10. Generate first 20 Fibonacci numbers
# 11. Find all prime numbers between 1 and 50
# 12. Create a pattern: print * in increasing then decreasing order

# Write your solutions below:
