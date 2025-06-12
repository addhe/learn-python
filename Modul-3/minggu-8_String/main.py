# This file contains exercises and examples related to strings in Python.

def string_examples():
    # Example of string creation
    greeting = "Hello, World!"
    print(greeting)

    # Example of string concatenation
    name = "Alice"
    welcome_message = greeting + " My name is " + name + "."
    print(welcome_message)

    # Example of string formatting
    age = 30
    formatted_message = f"{name} is {age} years old."
    print(formatted_message)

    # Example of string methods
    sample_string = "   Python Programming   "
    print("Original String:", sample_string)
    print("Stripped String:", sample_string.strip())
    print("Uppercase:", sample_string.upper())
    print("Lowercase:", sample_string.lower())
    print("Title Case:", sample_string.title())

if __name__ == "__main__":
    string_examples()