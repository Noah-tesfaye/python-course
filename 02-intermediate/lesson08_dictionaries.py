"""
LESSON 8: Dictionaries
======================
Dictionaries store data in key-value pairs. They're fast, flexible, and very useful.
"""

# CREATING DICTIONARIES
# ---------------------
print("=== CREATING DICTIONARIES ===")

# Empty dictionary
empty_dict = {}
also_empty = dict()

# Dictionary with items
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")

# Different value types
mixed = {
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6)
}
print(f"Mixed: {mixed}")

# Using dict() constructor
person2 = dict(name="Alice", age=25, city="London")
print(f"Person2: {person2}")

# Example of using static and dynamic dictionary creation:

# Static dictionary creation (using `{}`):
# This is when the dictionary structure and values are predefined.
static_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Static Dictionary: {static_dict}")

# Dynamic dictionary creation (using `dict()`):
# This is when the dictionary is created programmatically or dynamically.
keys = ["name", "age", "city"]
values = ["Bob", 30, "London"]
dynamic_dict = dict(zip(keys, values))
print(f"Dynamic Dictionary: {dynamic_dict}")

# Notes on when to use `dict()` and `{}`
# - Use `{}` for most cases, especially when defining dictionaries with static data.
# - Use `dict()` when:
#   - Creating dictionaries dynamically.
#   - Using keyword arguments for string keys.
#   - Converting other data structures (e.g., list of tuples) into a dictionary.
#
# Key Differences:
# 1. `{}` is more concise and commonly used.
# 2. `dict()` is useful for dynamic creation and keyword arguments.
# 3. `{}` is slightly faster than `dict()` because it avoids a function call.

# ACCESSING VALUES
# ----------------
print("\n=== ACCESSING VALUES ===")

student = {
    "name": "Emma",
    "grade": 95,
    "major": "Computer Science"
}

# Using square brackets
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")

# Using get() method (safer - doesn't error if key missing)
print(f"Major: {student.get('major')}")
print(f"GPA: {student.get('gpa', 'Not found')}")  # Default value

# ADDING AND MODIFYING
# --------------------
print("\n=== ADDING AND MODIFYING ===")

person = {"name": "John", "age": 30}
print(f"Original: {person}")

# Add new key-value pair
person["city"] = "New York"
print(f"After adding city: {person}")

# Modify existing value
person["age"] = 31
print(f"After modifying age: {person}")

# Update multiple values
person.update({"age": 32, "job": "Engineer"})
print(f"After update: {person}")

# REMOVING ITEMS
# --------------
print("\n=== REMOVING ITEMS ===")

person = {"name": "John", "age": 30, "city": "NYC", "job": "Engineer"}
print(f"Original: {person}")

# pop() - remove and return value
age = person.pop("age")
print(f"Popped age: {age}, Dict: {person}")

# popitem() - remove and return last item (Python 3.7+)
item = person.popitem()
print(f"Popped item: {item}, Dict: {person}")

# del - delete by key
del person["city"]
print(f"After del: {person}")

# clear() - remove all items
temp = {"a": 1, "b": 2}
temp.clear()
print(f"After clear: {temp}")

# DICTIONARY METHODS
# ------------------
print("\n=== DICTIONARY METHODS ===")
    
person = {"name": "Alice", "age": 25, "city": "Paris"}

# keys() - get all keys
print(f"Keys: {person.keys()}")
print(f"Keys as list: {list(person.keys())}")

# values() - get all values
print(f"Values: {person.values()}")
print(f"Values as list: {list(person.values())}")

# items() - get all key-value pairs
print(f"Items: {person.items()}")
print(f"Items as list: {list(person.items())}")

# CHECKING MEMBERSHIP
# -------------------
print("\n=== CHECKING MEMBERSHIP ===")

student = {"name": "Bob", "grade": 85, "major": "Physics"}

# Check if key exists
print(f"'name' in dict: {'name' in student}")
print(f"'gpa' in dict: {'gpa' in student}")

# Check if value exists (less efficient)
print(f"'Bob' in values: {'Bob' in student.values()}")

# LOOPING THROUGH DICTIONARIES
# -----------------------------
print("\n=== LOOPING THROUGH DICTIONARIES ===")

scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Loop through keys
print("Keys:")
for key in scores:
    print(f"  {key}")

# Loop through values
print("Values:")
for value in scores.values():
    print(f"  {value}")

# Loop through key-value pairs
print("Key-Value pairs:")
for key, value in scores.items():
    print(f"  {key}: {value}")

# NESTED DICTIONARIES
# -------------------
print("\n=== NESTED DICTIONARIES ===")

students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 92]
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grades": [78, 85, 88]
    }
}

print(f"Students: {students}")
print(f"Student1 name: {students['student1']['name']}")
print(f"Student2 first grade: {students['student2']['grades'][0]}")

# DICTIONARY COMPREHENSION
# ------------------------
print("\n=== DICTIONARY COMPREHENSION ===")

# Create dict of squares
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Create dict with condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transform existing dict
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Discounted: {discounted}")

# MERGING DICTIONARIES
# --------------------
print("\n=== MERGING DICTIONARIES ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: update()
merged = dict1.copy()
merged.update(dict2)
print(f"Merged with update: {merged}")

# Method 2: ** unpacking (Python 3.5+)
merged2 = {**dict1, **dict2}
print(f"Merged with unpacking: {merged2}")

# Method 3: | operator (Python 3.9+)
merged3 = dict1 | dict2
print(f"Merged with | operator: {merged3}")

# DICTIONARY WITH DEFAULT VALUES
# ------------------------------
print("\n=== DEFAULT VALUES ===")

from collections import defaultdict

# Regular dict with setdefault
word_count = {}
text = "hello world hello"
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word count: {word_count}")

# Using defaultdict
word_count2 = defaultdict(int)
for word in text.split():
    word_count2[word] += 1
print(f"Word count (defaultdict): {dict(word_count2)}")

# SORTING DICTIONARIES
# --------------------
print("\n=== SORTING DICTIONARIES ===")

scores = {"Alice": 85, "Charlie": 92, "Bob": 78, "David": 90}

# Sort by keys
sorted_by_key = dict(sorted(scores.items()))
print(f"Sorted by key: {sorted_by_key}")

# Sort by values
sorted_by_value = dict(sorted(scores.items(), key=lambda item: item[1]))
print(f"Sorted by value: {sorted_by_value}")

# Sort by values (descending)
sorted_desc = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted descending: {sorted_desc}")

# PRACTICAL EXAMPLES
# ------------------
print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Contact book
contacts = {
    "John": "555-1234",
    "Alice": "555-5678",
    "Bob": "555-9012"
}

name = "Alice"
if name in contacts:
    print(f"{name}'s number: {contacts[name]}")

# Example 2: Inventory system
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 45
}

# Sell some items
inventory["apples"] -= 5
print(f"Updated inventory: {inventory}")

# Example 3: Student database
students = {}

def add_student(id, name, age):
    students[id] = {"name": name, "age": age, "grades": []}

def add_grade(id, grade):
    if id in students:
        students[id]["grades"].append(grade)

add_student(1, "Alice", 20)
add_student(2, "Bob", 22)
add_grade(1, 95)
add_grade(1, 87)
print(f"Students database: {students}")

# Example 4: Character frequency
text = "hello world"
char_freq = {}
for char in text:
    if char != " ":
        char_freq[char] = char_freq.get(char, 0) + 1
print(f"Character frequency: {char_freq}")

# Example 5: Group items
items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
    {"name": "broccoli", "category": "vegetable"}
]

grouped = {}
for item in items:
    category = item["category"]
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(item["name"])

print(f"Grouped items: {grouped}")


# EXERCISES
# ----------
# 1. Create a dictionary of 5 countries and their capitals
# 2. Add a new country to the dictionary and update one capital
# 3. Loop through a dictionary and print all key-value pairs
# 4. Create a dictionary from two lists: one of keys, one of values
# 5. Count the frequency of each word in a sentence
# 6. Merge two dictionaries, keeping values from the second if keys overlap
# 7. Create a nested dictionary for a school with classes and students
# 8. Filter a dictionary to only include items where value > 50
# 9. Invert a dictionary (swap keys and values)
# 10. Find the key with the maximum value in a dictionary

# Write your solutions below:

# Example for Exercise 4:
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "NYC"]
# result = dict(zip(keys, values))
# print(result)

# Notes on `pop()` vs `del`

# - **`pop()`**:
#   - Removes and returns the value associated with the specified key.
#   - Safer: You can provide a default value to avoid errors if the key doesn't exist.
#   - Use Case: When you need the value of the removed item or want to handle missing keys gracefully.
# 
#   **Example**:
#   ```python
#   person = {"name": "Alice", "age": 25}
#   age = person.pop("age")  # Removes "age" and returns its value
#   print(age)  # Output: 25
#   print(person)  # Output: {'name': 'Alice'}
# 
#   # Using a default value
#   city = person.pop("city", "Not found")
#   print(city)  # Output: Not found
#   ```
# 
# - **`del`**:
#   - Removes the key-value pair from the dictionary but does not return the value.
#   - Raises an error if the key doesn't exist.
#   - Use Case: When you don't need the value of the removed item and are certain the key exists.
# 
#   **Example**:
#   ```python
#   person = {"name": "Alice", "age": 25}
#   del person["age"]  # Removes "age"
#   print(person)  # Output: {'name': 'Alice'}
# 
#   # Raises an error if the key doesn't exist
#   # del person["city"]  # KeyError: 'city'
#   ```
# 
# ### Key Differences
# | Feature         | `pop()`                          | `del`                          |
# |------------------|----------------------------------|--------------------------------|
# | **Returns Value** | Yes                             | No                             |
# | **Handles Missing Keys** | Can provide a default value | Raises `KeyError`             |
# | **Use Case**     | When you need the removed value | When you don't need the value |
