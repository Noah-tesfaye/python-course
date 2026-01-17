"""
LESSON 6: Lists
===============
Lists are ordered, mutable collections that can hold items of different types.
"""

# CREATING LISTS
# --------------
print("=== CREATING LISTS ===\n")

# Empty list
empty_list = []
also_empty = list()
print("Empty list:", empty_list)
print("Also empty:", also_empty)
print()

# List with items
numbers = [1, 2, 3, 4, 5]
print("Numbers list:", numbers)

fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)

mixed = [1, "hello", 3.14, True]
print("Mixed list:", mixed)

# ACCESSING LIST ELEMENTS
# -----------------------
print("\n" + "="*50)
print("=== ACCESSING ELEMENTS ===\n")

colors = ["red", "green", "blue", "yellow", "purple"]
print("Our list:", colors)
print()
print("colors[0] (first):", colors[0])
print("colors[2] (third):", colors[2])
print("colors[-1] (last):", colors[-1])
print("colors[-2] (second to last):", colors[-2])

# LIST SLICING
# ------------
print("\n" + "="*50)
print("=== LIST SLICING ===\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", numbers)
print()
print("numbers[:5] (first 5):", numbers[:5])
print("numbers[-3:] (last 3):", numbers[-3:])
print("numbers[3:7] (index 3 to 6):", numbers[3:7])
print("numbers[::2] (every 2nd):", numbers[::2])
print("numbers[::-1] (reversed):", numbers[::-1])

# MODIFYING LISTS
# ---------------
print("\n" + "="*50)
print("=== MODIFYING LISTS ===\n")

fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
print()

# Change an item
print("Changing fruits[1] to 'blueberry'...")
fruits[1] = "blueberry"
print("After change:", fruits)
print()

# Change multiple items
print("Changing fruits[0:2] to ['strawberry', 'mango']...")
fruits[0:2] = ["strawberry", "mango"]
print("After change:", fruits)

# LIST METHODS - ADDING ITEMS
# ----------------------------
print("\n" + "="*50)
print("=== ADDING ITEMS ===\n")

numbers = [1, 2, 3]
print("Starting list:", numbers)
print()

# append() - add to end
print("Using append(4)...")
numbers.append(4)
print("Result:", numbers)
print()

# insert() - add at specific position
print("Using insert(0, 0) - insert 0 at index 0...")
numbers.insert(0, 0)
print("Result:", numbers)
print()

# extend() - add multiple items
print("Using extend([5, 6, 7])...")
numbers.extend([5, 6, 7])
print("Result:", numbers)

# LIST METHODS - REMOVING ITEMS
# ------------------------------
print("\n" + "="*50)
print("=== REMOVING ITEMS ===\n")

fruits = ["apple", "banana", "cherry", "banana", "date"]
print("Starting list:", fruits)
print()

# remove() - remove first occurrence
print("Using remove('banana') - removes first 'banana'...")
fruits.remove("banana")
print("Result:", fruits)
print()

# pop() - remove and return item at index (default: last)
print("Using pop() - removes and RETURNS last item...")
popped = fruits.pop()
print("Returned value:", popped)
print("List now:", fruits)
print()

print("Using pop(0) - removes and RETURNS first item...")
popped_first = fruits.pop(0)
print("Returned value:", popped_first)
print("List now:", fruits)
print()

# del - delete by index or slice
print("--- Using del ---")
numbers = [0, 1, 2, 3, 4, 5]
print("Starting list:", numbers)
print("Using del numbers[2] - deletes index 2...")
del numbers[2]
print("Result:", numbers)
print()

# del can also remove slices (pop cannot!)
numbers = [0, 1, 2, 3, 4, 5]
print("Starting list:", numbers)
print("Using del numbers[1:4] - deletes index 1, 2, 3...")
del numbers[1:4]
print("Result:", numbers)
print()

# KEY DIFFERENCE: pop() vs del
print("--- KEY DIFFERENCE: pop() vs del ---")
print()

# pop() RETURNS the removed value
list1 = [10, 20, 30, 40]
print("List:", list1)
print("Using pop(2)...")
removed_value = list1.pop(2)
print("  Returned value:", removed_value)
print("  List now:", list1)
print()

# del does NOT return anything, just removes
list2 = [10, 20, 30, 40]
print("List:", list2)
print("Using del list2[2]...")
del list2[2]
print("  Returns: Nothing")
print("  List now:", list2)
print()

# pop() removes ONE item, del can remove MULTIPLE
list3 = [0, 1, 2, 3, 4, 5]
print("List:", list3)
print("Using del list3[1:4] - removes multiple items...")
del list3[1:4]
print("Result:", list3)
print()

# clear() - remove all items
temp = [1, 2, 3]
print("Using clear() on", temp)
temp.clear()
print("Result:", temp)

# LIST METHODS - ORGANIZING
# --------------------------
print("\n" + "="*50)
print("=== ORGANIZING LISTS ===\n")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original list:", numbers)
print()

# sort() - sort in place
print("Using sort() - sorts the list from low to high...")
numbers.sort()
print("Result:", numbers)
print()

# sort in reverse
print("Using sort(reverse=True) - sorts high to low...")
numbers.sort(reverse=True)
print("Result:", numbers)
print()

# reverse() - reverse order
print("Using reverse() - just flips the order...")
numbers.reverse()
print("Result:", numbers)
print()

# sorted() - return sorted copy (doesn't modify original)
print("--- sorted() vs sort() ---")
original = [3, 1, 4, 1, 5]
print("Original list:", original)
print("Using sorted(original) - creates NEW sorted list...")
sorted_copy = sorted(original)
print("  Original list:", original, "(unchanged!)")
print("  New sorted list:", sorted_copy)

# LIST METHODS - SEARCHING
# -------------------------
print("\n" + "="*50)
print("=== SEARCHING IN LISTS ===\n")

fruits = ["apple", "banana", "cherry", "banana"]
print("Our list:", fruits)
print()

# count() - count occurrences
print("How many 'banana'?")
print("  fruits.count('banana'):", fruits.count('banana'))
print()

# index() - find first occurrence
print("Where is 'cherry'?")
print("  fruits.index('cherry'):", fruits.index('cherry'))
print()

# in operator - check if item exists
print("Is 'apple' in the list?")
print("  'apple' in fruits:", 'apple' in fruits)
print()
print("Is 'grape' in the list?")
print("  'grape' in fruits:", 'grape' in fruits)

# LIST OPERATIONS
# ---------------
print("\n" + "="*50)
print("=== LIST OPERATIONS ===\n")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List 1:", list1)
print("List 2:", list2)
print()

# Concatenation
print("Combining lists: list1 + list2")
combined = list1 + list2
print("Result:", combined)
print()

# Repetition
print("Repeating list: list1 * 3")
repeated = list1 * 3
print("Result:", repeated)
print()

# Length
print("Length of list1:")
print("  len(list1):", len(list1))
print()

# Min, Max, Sum (for numbers)
numbers = [5, 2, 8, 1, 9]
print("Numbers:", numbers)
print("  min(numbers):", min(numbers))
print("  max(numbers):", max(numbers))
print("  sum(numbers):", sum(numbers))

# LIST COMPREHENSION
# ------------------
print("\n" + "="*50)
print("=== LIST COMPREHENSION ===\n")

# Create list of squares
print("Create squares of 1 to 5:")
print("  [x**2 for x in range(1, 6)]")
squares = [x**2 for x in range(1, 6)]
print("  Result:", squares)
print()

# Create list with condition
print("Get even numbers from 1 to 10:")
print("  [x for x in range(1, 11) if x % 2 == 0]")
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("  Result:", even_numbers)
print()

# Transform existing list
fruits = ["apple", "banana", "cherry"]
print("Convert to uppercase:", fruits)
print("  [fruit.upper() for fruit in fruits]")
upper_fruits = [fruit.upper() for fruit in fruits]
print("  Result:", upper_fruits)

# NESTED LISTS (2D Lists)
# -----------------------
print("\n" + "="*50)
print("=== NESTED LISTS ===\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D Matrix:")
for row in matrix:
    print(" ", row)
print()
print("matrix[0] (first row):", matrix[0])
print("matrix[1][2] (row 1, column 2):", matrix[1][2])

# COPYING LISTS
# -------------
print("\n" + "="*50)
print("=== COPYING LISTS ===\n")

original = [1, 2, 3]
print("Original list:", original)
print()

# Wrong way (creates reference)
print("WRONG WAY - reference = original")
reference = original
print("Changing reference...")
reference.append(4)
print("  Reference:", reference)
print("  Original:", original, "← ALSO CHANGED! (Bad!)")
print()

# Right way - shallow copy
original = [1, 2, 3]
print("RIGHT WAY - copy1 = original.copy()")
copy1 = original.copy()
print("Changing copy1...")
copy1.append(4)
print("  Copy:", copy1)
print("  Original:", original, "← Unchanged! (Good!)")

# PRACTICAL EXAMPLES
# ------------------
print("\n" + "="*50)
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Shopping list
print("Example 1: Shopping List")
shopping_list = []
shopping_list.append("milk")
shopping_list.append("eggs")
shopping_list.append("bread")
print("  Shopping list:", shopping_list)
print()

# Example 2: Grade calculator
print("Example 2: Grade Calculator")
grades = [85, 92, 78, 90, 88]
average = sum(grades) / len(grades)
print("  Grades:", grades)
print("  Average:", average, "→", f"{average:.2f}")
print()

# Example 3: Remove duplicates
print("Example 3: Remove Duplicates")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print("  Original:", numbers)
print("  Unique:", unique)

# EXERCISES
# ----------
# 1. Create a list of your 5 favorite movies and print the second one
# 2. Create a list of numbers 1-10, then create a new list with only odd numbers
# 3. Create a list and add items using append, then sort it in reverse order
# 4. Find the maximum and minimum values in [45, 23, 67, 12, 89, 34]
# 5. Create a list of temperatures in Celsius, convert to Fahrenheit using list comprehension
# 6. Remove all instances of a specific value from a list
# 7. Create a 3x3 matrix and print the diagonal elements

# Write your solutions below:
