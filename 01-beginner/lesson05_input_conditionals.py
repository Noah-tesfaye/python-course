"""
LESSON 5: User Input and Conditional Statements
================================================
Learn how to get input from users and make decisions in your code.
"""

# USER INPUT
# ----------
print("=== USER INPUT ===")

# input() function always returns a string
# Uncomment the lines below to test (commented to avoid blocking during demos)

# name = input("What is your name? ")
# print(f"Hello, {name}!")

# # Converting input to numbers
# age = int(input("What is your age? "))
# print(f"Next year you'll be {age + 1}!")

# For demonstration, we'll use predefined values
name = "Noah"
age = 25
print(f"Name: {name}, Age: {age}")

# IF STATEMENTS
# -------------
print("\n=== IF STATEMENTS ===")

# Basic if statement
temperature = 75

if temperature > 70:
    print("It's warm outside!")
    print("Wear light clothes.")

# IF-ELSE STATEMENTS
# ------------------
print("\n=== IF-ELSE ===")

age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# IF-ELIF-ELSE STATEMENTS
# -----------------------
print("\n=== IF-ELIF-ELSE ===")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# NESTED IF STATEMENTS
# --------------------
print("\n=== NESTED IF ===")

age = 20
has_license = True

if age >= 18:
    print("You are old enough to drive.")
    if has_license:
        print("You can drive!")
    else:
        print("But you need a license.")
else:
    print("You are too young to drive.")

# MULTIPLE CONDITIONS
# -------------------
print("\n=== MULTIPLE CONDITIONS ===")

# Using AND
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the concert.")

# Using OR
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")

# Using NOT
is_raining = False

if not is_raining:
    print("Let's go for a walk!")

# COMPARISON CHAINS
# -----------------
print("\n=== COMPARISON CHAINS ===")

x = 15

# Check if x is between 10 and 20
if 10 < x < 20:
    print(f"{x} is between 10 and 20")

# Check if x is outside range
if x < 10 or x > 20:
    print(f"{x} is outside the range")

# TERNARY OPERATOR (Conditional Expression)
# ------------------------------------------
print("\n=== TERNARY OPERATOR ===")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Useful for simple assignments
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

# PRACTICAL EXAMPLES
# ------------------
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: BMI Calculator
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

print(f"BMI: {bmi:.1f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Example 2: Password validator
password = "python123"
min_length = 8

if len(password) >= min_length:
    if any(char.isdigit() for char in password):
        print("Password is strong!")
    else:
        print("Password should contain numbers.")
else:
    print(f"Password must be at least {min_length} characters.")

# Example 3: Discount calculator
price = 100
is_member = True

if is_member:
    discount = 0.2  # 20% discount
    final_price = price * (1 - discount)
    print(f"Member price: ${final_price:.2f}")
else:
    print(f"Regular price: ${price:.2f}")

# MATCH-CASE STATEMENTS (Python 3.10+)
# -------------------------------------
print("\n=== MATCH-CASE (Python 3.10+) ===")

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("It's a regular day")

# EXERCISES
# ----------
# 1. Ask user for a number and check if it's positive, negative, or zero
# 2. Create a simple calculator: ask for two numbers and an operator (+, -, *, /)
# 3. Check if a year is a leap year (divisible by 4, but not 100, unless also by 400)
# 4. Create a grade calculator: input score (0-100) and output letter grade
# 5. Check if a person can vote: must be 18+ and a citizen
# 6. Temperature converter: ask for temp and unit (C/F), convert to the other unit

# Write your solutions below:

# Example template for Exercise 1:
# number = int(input("Enter a number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")
