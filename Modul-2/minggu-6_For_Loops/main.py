# For Loops Example

# This script demonstrates the use of for loops in Python.

# Example 1: Basic for loop
print("Example 1: Basic for loop")
for i in range(5):
    print(f"Iteration {i}")

# Example 2: Looping through a list
print("\nExample 2: Looping through a list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Example 3: Using for loop with enumerate
print("\nExample 3: Using for loop with enumerate")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Example 4: Nested for loops
print("\nExample 4: Nested for loops")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")