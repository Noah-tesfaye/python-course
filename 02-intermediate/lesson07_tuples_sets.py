"""
LESSON 7: Tuples and Sets
==========================
Learn about tuples (immutable sequences) and sets (unordered unique collections).
"""

# UNDERSTANDING MUTABLE vs IMMUTABLE
# ==================================
print("=== WHAT IS MUTABLE AND IMMUTABLE? ===")

# Think of it like this:
# MUTABLE = Can be changed (like a whiteboard - you can erase and rewrite)
# IMMUTABLE = Cannot be changed (like a printed book - once printed, text stays the same)

# MUTABLE example - Lists CAN be changed
print("\n--- MUTABLE (Lists) ---")
my_list = [1, 2, 3]
print(f"Original list: {my_list}")

my_list[0] = 100  # We can change the first item!
print(f"After changing first item: {my_list}")

my_list.append(4)  # We can add items!
print(f"After adding item: {my_list}")

# The list changes in place - same list, different contents

# IMMUTABLE example - Strings CANNOT be changed
print("\n--- IMMUTABLE (Strings) ---")
my_string = "Hello"
print(f"Original string: {my_string}")

# This would cause an error:
# my_string[0] = "J"  # TypeError: 'str' object does not support item assignment

# To "change" a string, you must create a NEW string
new_string = "J" + my_string[1:]
print(f"New string: {new_string}")
print(f"Original string is still: {my_string}")

# SUMMARY:
# --------
# MUTABLE (can change):     list, dict, set
# IMMUTABLE (cannot change): int, float, str, tuple, frozenset
#
# Why does this matter?
# 1. Immutable objects are safer - they can't be accidentally changed
# 2. Immutable objects can be used as dictionary keys
# 3. Tuples are immutable lists - once created, they stay the same!

print("\n" + "="*50)
print("Now let's learn about TUPLES (immutable lists)!")
print("="*50)

# TUPLES
# ======

# CREATING TUPLES
# ---------------
print("=== CREATING TUPLES ===")

# Empty tuple
empty_tuple = ()
also_empty = tuple()

# Tuple with items
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True)

# Single item tuple (need comma)
single = (42,)  # Note the comma!
not_tuple = (42)  # This is just an integer

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Single tuple: {single}, type: {type(single)}")
print(f"Not tuple: {not_tuple}, type: {type(not_tuple)}")

# Notes on empty tuples vs static/dynamic tuples:
# - `empty_tuple = ()` and `also_empty = tuple()` both create an empty tuple. They are equivalent.
# - These are not examples of static or dynamic tuples because they contain no values.
#
# Static Tuple:
# - A tuple with predefined values at the time of creation.
#   Example: static_tuple = (1, 2, 3)
#
# Dynamic Tuple:
# - A tuple created programmatically, often using functions or loops.
#   Example: dynamic_tuple = tuple(range(1, 4))  # Creates (1, 2, 3)

# ACCESSING TUPLE ELEMENTS
# -------------------------
print("\n=== ACCESSING TUPLE ELEMENTS ===")

colors = ("red", "green", "blue", "yellow")
print(f"Colors: {colors}")
print(f"First: {colors[0]}")
print(f"Last: {colors[-1]}")
print(f"Slice [1:3]: {colors[1:3]}")

# TUPLE OPERATIONS
# ----------------
print("\n=== TUPLE OPERATIONS ===")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Length
print(f"Length: {len(tuple1)}")

# Count and index
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# TUPLE IMMUTABILITY
# ------------------
print("\n=== TUPLE IMMUTABILITY ===")

coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# This would cause an error:
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# However, you can create a new tuple
new_coordinates = (15, 20)
print(f"New coordinates: {new_coordinates}")

# TUPLE UNPACKING
# ---------------
print("\n=== TUPLE UNPACKING ===")

# Basic unpacking
point = (3, 4)
x, y = point
print(f"x: {x}, y: {y}")

# Multiple values
person = ("John", 25, "USA")
name, age, country = person
print(f"Name: {name}, Age: {age}, Country: {country}")

# Swap values
a = 5
b = 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# WHEN TO USE TUPLES
# ------------------
print("\n=== WHEN TO USE TUPLES ===")

# 1. For coordinates
location = (40.7128, -74.0060)  # Latitude, Longitude
print(f"Location: {location}")

# 2. Return multiple values from function
def get_user_info():
    return ("Alice", 30, "alice@example.com")

name, age, email = get_user_info()
print(f"User: {name}, {age}, {email}")

# 3. Dictionary keys (tuples are hashable, lists are not)
# ---------------------------------------------------------
# What does "hashable" mean?
# Think of a hash like a fingerprint - it's a unique number that represents an object.
# For dictionary keys, Python needs to calculate this "fingerprint" to quickly find values.
#
# Why can tuples be dictionary keys but lists cannot?
# - TUPLES are IMMUTABLE (can't change) → their "fingerprint" stays the same → can be used as keys
# - LISTS are MUTABLE (can change) → their "fingerprint" would change → CANNOT be used as keys
#
# If a list could be a key and you changed the list, Python wouldn't be able to find
# the value anymore because the "fingerprint" changed!

print("\n--- Using tuples as dictionary keys ---")
# Tuples work perfectly as dictionary keys
locations = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(f"Locations dict: {locations}")
print(f"Location at (1, 2): {locations[(1, 2)]}")

# This WORKS because tuples are immutable:
coordinates = (2, 3)
locations[coordinates] = "Point C"
print(f"Added new location: {locations}")

# This would FAIL with an error:
# bad_locations = {
#     [0, 0]: "Origin"  # TypeError: unhashable type: 'list'
# }
#
# Lists cannot be keys because they can change:
# key = [1, 2]
# bad_dict = {key: "value"}  # Error!
# key.append(3)  # If this worked, Python couldn't find "value" anymore!

print("Rule: Only immutable types can be dictionary keys!")
print("✓ Can use: int, float, str, tuple")
print("✗ Cannot use: list, dict, set")

# SETS
# ====

# CREATING SETS
# -------------
print("\n=== CREATING SETS ===")

# Empty set (use set(), not {})
empty_set = set()
# empty_dict = {}  # This creates a dict, not a set!

# IMPORTANT: Understanding {} curly braces
# ----------------------------------------
# {} can create EITHER a set OR a dictionary depending on what's inside!
#
# {} with NOTHING        → Dictionary (empty)
# {1, 2, 3}             → Set (just values)
# {"key": "value"}      → Dictionary (key:value pairs with colon)
#
# Think of it this way:
# - If you see a COLON (:) inside → it's a DICTIONARY
# - If you see just VALUES → it's a SET

print("\n--- Sets vs Dictionaries with {} ---")
# This is a SET (no colons, just values)
my_set = {1, 2, 3, 4, 5}
print(f"Set: {my_set}, type: {type(my_set)}")

# This is a DICTIONARY (has colons for key:value pairs)
my_dict = {"name": "John", "age": 25}
print(f"Dictionary: {my_dict}, type: {type(my_dict)}")

# This is also a SET (just values, even though they're strings)
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}, type: {type(fruits)}")

# Sets automatically remove duplicates
# When you create a set with duplicate values, Python keeps only one of each
numbers_with_dupes = {1, 2, 2, 3, 3, 3, 4}
print(f"Duplicates removed: {numbers_with_dupes}")
print("Notice: Even though we wrote 2 three times and 3 three times, the set only kept one of each!")

# Create set from list
list_numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(list_numbers)
print(f"From list: {unique_numbers}")

# ADDING AND REMOVING
# -------------------
print("\n=== ADDING AND REMOVING ===")

fruits = {"apple", "banana"}
print(f"Original: {fruits}")

# add() - add single item
fruits.add("cherry")
print(f"After add: {fruits}")

# update() - add multiple items
fruits.update(["date", "elderberry"])
print(f"After update: {fruits}")

# remove() - remove item (raises error if not found)
fruits.remove("banana")
print(f"After remove: {fruits}")

# discard() - remove item (no error if not found)
fruits.discard("fig")  # No error even though 'fig' isn't there
print(f"After discard: {fruits}")

# pop() - remove and return arbitrary item
popped = fruits.pop()
print(f"Popped: {popped}, Remaining: {fruits}")

# clear() - remove all
temp = {1, 2, 3}
temp.clear()
print(f"After clear: {temp}")

# SET OPERATIONS
# --------------
print("\n=== SET OPERATIONS ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union (all items from both sets)
union = set_a | set_b
# or: union = set_a.union(set_b)
print(f"Union: {union}")

# Intersection (items in both sets)
intersection = set_a & set_b
# or: intersection = set_a.intersection(set_b)
print(f"Intersection: {intersection}")

# Difference (items in A but not in B)
difference = set_a - set_b
# or: difference = set_a.difference(set_b)
print(f"Difference (A-B): {difference}")

# Symmetric difference (items in either set, but not both)
sym_diff = set_a ^ set_b
# or: sym_diff = set_a.symmetric_difference(set_b)
print(f"Symmetric difference: {sym_diff}")

# SET METHODS
# -----------
print("\n=== SET METHODS ===")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Subset
subset = {1, 2}
print(f"Is {subset} subset of {set_a}? {subset.issubset(set_a)}")

# Superset
print(f"Is {set_a} superset of {subset}? {set_a.issuperset(subset)}")

# Disjoint (no common elements)
set_c = {7, 8, 9}
print(f"Are {set_a} and {set_c} disjoint? {set_a.isdisjoint(set_c)}")

# SET COMPREHENSION
# -----------------
print("\n=== SET COMPREHENSION ===")

# Create set of squares
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Create set with condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# FROZEN SETS
# -----------
print("\n=== FROZEN SETS ===")

# Immutable version of set
frozen = frozenset([1, 2, 3, 4])
print(f"Frozen set: {frozen}")

# Can be used as dictionary key
location_data = {
    frozenset([1, 2]): "Location A",
    frozenset([3, 4]): "Location B"
}
print(f"Dict with frozenset keys: {location_data}")

# PRACTICAL EXAMPLES
# ------------------
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Remove duplicates from list
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique = list(set(numbers))
print(f"Unique numbers: {unique}")

# Example 2: Find common items
list1 = ["apple", "banana", "cherry", "date"]
list2 = ["cherry", "date", "elderberry", "fig"]
common = set(list1) & set(list2)
print(f"Common items: {common}")

# Example 3: Find all unique characters in a string
text = "hello world"
unique_chars = set(text)
print(f"Unique characters: {unique_chars}")

# Example 4: Student attendance
monday = {"Alice", "Bob", "Charlie", "David"}
tuesday = {"Bob", "Charlie", "Eve", "Frank"}

# Students who attended both days
both_days = monday & tuesday
print(f"Attended both: {both_days}")

# All students
all_students = monday | tuesday
print(f"All students: {all_students}")

# Only Monday
only_monday = monday - tuesday
print(f"Only Monday: {only_monday}")

# EXERCISES
# ----------
# 1. Create a tuple of 5 cities and unpack them into separate variables
# 2. Write a function that returns multiple values using a tuple
# 3. Create two sets of numbers and find their union, intersection, and difference
# 4. Remove duplicates from the list [1,2,3,2,4,3,5,1] using sets
# 5. Check if one set is a subset of another
# 6. Find all unique words in a sentence
# 7. Create a set of even numbers from 1-20 using set comprehension

# Write your solutions below:
