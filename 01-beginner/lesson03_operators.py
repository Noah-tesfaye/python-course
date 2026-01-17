"""
LESSON 3: Operators
===================
Operators perform operations on variables and values.
"""

# ARITHMETIC OPERATORS
# --------------------
print("=== ARITHMETIC OPERATORS ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")  # Returns float
print(f"Floor Division: {a} // {b} = {a // b}")  # Returns integer (rounds down)
print(f"Modulus (remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")  # 10 to the power of 3

# COMPARISON OPERATORS
# --------------------
print("\n=== COMPARISON OPERATORS ===")
# Return True or False

x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"Equal to: {x} == {y} is {x == y}")
print(f"Not equal to: {x} != {y} is {x != y}")
print(f"Greater than: {x} > {y} is {x > y}")
print(f"Less than: {x} < {y} is {x < y}")
print(f"Greater than or equal: {x} >= {y} is {x >= y}")
print(f"Less than or equal: {x} <= {y} is {x <= y}")

# LOGICAL OPERATORS
# -----------------
print("\n=== LOGICAL OPERATORS ===")
# and, or, not

is_sunny = True
is_warm = False

print(f"is_sunny = {is_sunny}, is_warm = {is_warm}")
print(f"AND: is_sunny and is_warm = {is_sunny and is_warm}")
print(f"OR: is_sunny or is_warm = {is_sunny or is_warm}")
print(f"NOT: not is_sunny = {not is_sunny}")

# ASSIGNMENT OPERATORS
# --------------------
print("\n=== ASSIGNMENT OPERATORS ===")

num = 10
print(f"Initial value: {num}")

num += 5  # Same as num = num + 5
print(f"After += 5: {num}")

num -= 3  # Same as num = num - 3
print(f"After -= 3: {num}")

num *= 2  # Same as num = num * 2
print(f"After *= 2: {num}")

num /= 4  # Same as num = num / 4
print(f"After /= 4: {num}")

# MEMBERSHIP OPERATORS
# --------------------
print("\n=== MEMBERSHIP OPERATORS ===")
# in, not in (check if value exists in sequence)

text = "Hello, Python!"
print(f"Text: {text}")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'Java' not in text: {'Java' not in text}")

# IDENTITY OPERATORS
# ------------------
print("\n=== IDENTITY OPERATORS ===")
# is, is not (check if objects are the same)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a is c: {a is c}")  # True (same object)
print(f"a is b: {a is b}")  # False (different objects)
print(f"a == b: {a == b}")  # True (same values)

# OPERATOR PRECEDENCE
# --------------------
print("\n=== OPERATOR PRECEDENCE ===")
# Order: () -> ** -> *, /, //, % -> +, - -> comparisons -> not -> and -> or

result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # Multiplication first

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # Parentheses first

result3 = 10 + 5 * 2 ** 3
print(f"10 + 5 * 2 ** 3 = {result3}")  # Exponent, then multiplication, then addition

# EXERCISES
# ----------
# 1. Calculate the area of a rectangle with width 15 and height 7
# 2. Check if a number is even (use modulus operator)
# 3. Calculate compound interest: P * (1 + r) ** t, where P=1000, r=0.05, t=3
# 4. Check if a number is between 10 and 20 (use logical operators)
# 5. Use floor division to find how many dozens in 50 eggs

# Write your solutions below:
