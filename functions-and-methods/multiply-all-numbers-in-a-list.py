# Write a Python function to multiply all the numbers in a list


def multiply(numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total


print(multiply([1, 1, 2, 4, 8, 16, 32, 64, 128]))
