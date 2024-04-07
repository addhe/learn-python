"""Write a python function that accepts a string and calculate the number of upper case
letters and lower case letters"""


def up_low(s):
    dict = {"upper": 0, "lower": 0}

    for char in s:
        if char.isupper():
            dict["upper"] += 1
        elif char.islower():
            dict["lower"] += 1
        else:
            pass
    print(f"Original String: {s}")
    print(f'Lowercase Count: {dict["upper"]}')
    print(f'Uppercase Count: {dict["lower"]}')


s = "Hai Mr. Awan, how are you today? would you like a Coffee?"

up_low(s)
