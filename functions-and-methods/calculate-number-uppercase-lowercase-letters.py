"""Write a python function that accepts a string and calculate the number of upper case
letters and lower case letters"""


def up_low(s):
    lowercase = 0
    uppercase = 0

    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f"Original String: {s}")
    print(f"Lowercase Count: {lowercase}")
    print(f"Uppercase Count: {uppercase}")


s = "Hai Mr. Awan, how are you today? would you like a Coffee?"

up_low(s)
