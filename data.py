# append():
# Purpose: Adds a single element to the end of a list.
# Syntax: list.append(element)

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# Output: [1, 2, 3, 4]

# # remove():
# Purpose: Removes the first occurrence of a specified value from the list. If the value is not present, it raises a ValueError.
# Syntax: list.remove(value)

my_list = ['apple', 'banana', 'cherry', 'banana']
my_list.remove('banana')
print(my_list)
# Output: ['apple', 'cherry', 'banana']

# pop():
# Purpose: Removes and returns the element at a specified index. If no index is provided, it removes and returns the last element of the list.
# Syntax: list.pop(index=-1) (index is optional, defaults to -1 for the last element)

my_list = [10, 20, 30, 40]
popped_item = my_list.pop(1) # Removes element at index 1 (20)
print(popped_item)
# Output: 20
print(my_list)
# Output: [10, 30, 40]

last_item = my_list.pop() # Removes the last element (40)
print(last_item)
# Output: 40
print(my_list)
# Output: [10, 30]

# len():
# Purpose: This is a built-in Python function (not a list method) that returns the number of items (length) in an object, such as a list.
# Syntax: len(object)

my_list = ['a', 'b', 'c']
list_length = len(my_list)
print(list_length)
# Output: 3


# Tuples
# Usage: Store a fixed collection of items that should not be altered. For example, storing coordinates, user credentials, or configuration values.
# Mutability: Immutable, meaning you cannot change, add, or remove elements after creation.
# Syntax: Enclosed in parentheses () or a comma-separated list.
# Access: Ordered, so elements can be accessed by index (starting from 0).


my_tuple = (1, 2, 3, "hello", "world", 5, 6, 7)
print(my_tuple[4]) # Output: 1
# my_tuple[0] = 5  # This would cause an error


# Python dictionaries are powerful data structures for storing data in key-value pairs.
# Keys:
# Keys are unique identifiers within a dictionary, used to access their corresponding values.
# Keys must be immutable data types (e.g., strings, numbers, tuples). Lists or other dictionaries cannot be used as keys.
# Values:
# Values are the data associated with each key.
# Values can be of any data type, including other dictionaries, lists, or custom objects.
# Updating Dictionaries:
# Updating an existing value:
# To change the value associated with an existing key, simply assign a new value to that key using the assignment operator (=).


my_dict = {"name": "Alice", "age": 30}
my_dict["age"] = 31  # Updates the value for the "age" key
print(my_dict)
# Output: {'name': 'Alice', 'age': 31}

# Adding a new key-value pair:
# If you assign a value to a key that does not yet exist in the dictionary, a new key-value pair will be added.

my_dict = {"name": "Bob"}
my_dict["city"] = "New York"  # Adds a new key-value pair
print(my_dict)
# Output: {'name': 'Bob', 'city': 'New York'}

# Using the update() method:
# The update() method allows you to add or update multiple key-value pairs at once, either from another dictionary or from an iterable of key-value pairs.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # Updates dict1 with key-value pairs from dict2
print(dict1)
# Output: {'a': 1, 'b': 3, 'c': 4}

dict3 = {"x": 10}
dict3.update(y=20, z=30) # Updates dict3 with new key-value pairs
print(dict3)
# Output: {'x': 10, 'y': 20, 'z': 30}

# Using the merge | and update |= operators (Python 3.9+):
# The merge operator | creates a new dictionary by combining two dictionaries. If keys overlap, the value from the right-hand dictionary takes precedence.
# The update operator |= updates a dictionary in-place, similar to update().

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged_dict = d1 | d2  # Creates a new dictionary
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}

d1 |= d2  # Updates d1 in-place
print(d1)
# Output: {'a': 1, 'b': 3, 'c': 4}

# Basic Math Operations (Arithmetic Operators):
# Python's built-in arithmetic operators allow for common mathematical calculations:
# Addition: +
# Subtraction: -
# Multiplication: *
# Division (float result): /
# Floor Division (integer result, discarding remainder): //
# Modulus (remainder of division): %
# Exponentiation: **

a = 10
b = 3

print(f"Addition: {a + b}")        # Output: 13
print(f"Subtraction: {a - b}")     # Output: 7
print(f"Multiplication: {a * b}")  # Output: 30
print(f"Division: {a / b}")        # Output: 3.3333333333333335
print(f"Floor Division: {a // b}") # Output: 3
print(f"Modulus: {a % b}")         # Output: 1
print(f"Exponentiation: {a ** b}") # Output: 1000

# math Module Functions:
# The math module provides a wide array of mathematical functions and constants. To use them, it must be imported: 

import math

#Some common functions and constants include:
# Some common functions and constants include:
# math.sqrt(x): Returns the square root of x.
# math.pow(x, y): Returns x raised to the power of y.
# math.ceil(x): Returns the smallest integer greater than or equal to x.
# math.floor(x): Returns the largest integer less than or equal to x.
# math.factorial(x): Returns the factorial of x.
# math.log(x, base): Returns the logarithm of x to the given base. If base is not specified, it defaults to e.
# math.sin(x), math.cos(x), math.tan(x): Trigonometric functions (input in radians).
# math.degrees(x), math.radians(x): Convert angles between degrees and radians.
# math.pi: The mathematical constant pi (π).
# math.e: The mathematical constant e.

import math

print(f"Square root of 16: {math.sqrt(16)}") # Output: 4.0
print(f"2 to the power of 3: {math.pow(2, 3)}") # Output: 8.0
print(f"Ceiling of 3.7: {math.ceil(3.7)}") # Output: 4
print(f"Floor of 3.7: {math.floor(3.7)}") # Output: 3
print(f"Factorial of 5: {math.factorial(5)}") # Output: 120
print(f"Log base 10 of 100: {math.log10(100)}") # Output: 2.0
print(f"Value of pi: {math.pi}") # Output: 3.141592653589793