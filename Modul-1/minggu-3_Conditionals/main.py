# This file contains exercises or examples related to conditionals in Python.

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage
if __name__ == "__main__":
    test_numbers = [10, -5, 0]
    for number in test_numbers:
        result = check_number(number)
        print(f"The number {number} is {result}.")