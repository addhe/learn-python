"""
    # Conditionals
    # Conditionals di python adalah pernyataan yang digunakan untuk mengecek suatu kondisi
    # jika kondisi tersebut benar maka pernyataan tersebut akan dieksekusi
    # jika kondisi tersebut salah maka pernyataan tersebut tidak akan dieksekusi
    # Comparison operators
    # ==  : sama dengan
    # !=  : tidak sama dengan
    # >   : lebih besar dari
    # <   : lebih kecil dari
    # >=  : lebih besar dari atau sama dengan
    # <=  : lebih kecil dari atau sama dengan
"""


# Conditional Statements
print("Conditional Statements")
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# Nested Conditional Statements
print("Nested Conditional Statements")
x = 10
y = 5
if x > 0:
    if y > 0:
        print("x and y are positive")
    else:
        print("x is positive and y is not positive")
else:
    if y > 0:
        print("x is not positive and y is positive")
    else:
        print("x and y are not positive")

# Ternary Operator
print("Ternary Operator")
x = 10
y = 5
result = "x is greater than y" if x > y else "x is not greater than y"
print(result)

# Switch Case Statement
print("Switch Case Statement")
x = 1
def switch_case(x):
    switcher = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3",
    }
    return switcher.get(x, "Invalid case")
print(switch_case(x))

# match case statement
print("Match Case Statement")
x = 1
match x:
    case 1:
        print("Case 1")
    case 2:
        print("Case 2")
    case 3:
        print("Case 3")
    case _:
        print("Invalid case")

# Branching with if-statements
print("Branching with if-statements")
x = 10
y = 5
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# elif statement
print("elif statement")
x = 10
y = 5
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# if statement
print("if statement")
x = 10
y = 5
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# complex branching with if-statements
print("Complex branching with if-statements")
x = 10
y = 5
if x > y:
    print("x is greater than y")
    if x > 0:
        print("x is positive")
    else:
        print("x is negative")
elif x < y:
    print("x is less than y")
    if x > 0:
        print("x is positive")
    else:
        print("x is negative")
else:
    print("x is equal to y")
    if x > 0:
        print("x is positive")
    else:
        print("x is negative")


# Comparison Operators with Strings
print("Comparison Operators with Strings")
print("Hello" == "Hello")  # True
print("Hello" != "Hello")  # False
print("Hello" > "Hello")  # False
print("Hello" < "Hello")  # False
print("Hello" >= "Hello")  # True
print("Hello" <= "Hello")  # True
print("Hello" == "hello")  # False
print("Hello" != "hello")  # True
print("Hello" > "hello")  # False
print("Hello" < "hello")  # True
print("Hello" >= "hello")  # False
print("Hello" <= "hello")  # True
print("Hello" == "HELLO")  # False

# Comparison Operators with Numbers
print("Comparison Operators with Numbers")
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True
print(1 == 2)  # False
print(1 != 2)  # True
print(1 > 2)  # False
print(1 < 2)  # True
print(1 >= 2)  # False
print(1 <= 2)  # True

# Comparison Operators with Lists
print("Comparison Operators with Lists")
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] != [1, 2, 3])  # False
print([1, 2, 3] > [1, 2, 3])  # False
print([1, 2, 3] < [1, 2, 3])  # False
print([1, 2, 3] >= [1, 2, 3])  # True
print([1, 2, 3] <= [1, 2, 3])  # True
print([1, 2, 3] == [1, 2, 4])  # False
print([1, 2, 3] != [1, 2, 4])  # True
print([1, 2, 3] > [1, 2, 4])  # False
print([1, 2, 3] < [1, 2, 4])  # True
print([1, 2, 3] >= [1, 2, 4])  # False
print([1, 2, 3] <= [1, 2, 4])  # True

# Comparison Operators with Tuples
print("Comparison Operators with Tuples")
print((1, 2, 3) == (1, 2, 3))  # True
print((1, 2, 3) != (1, 2, 3))  # False
print((1, 2, 3) > (1, 2, 3))  # False
print((1, 2, 3) < (1, 2, 3))  # False
print((1, 2, 3) >= (1, 2, 3))  # True
print((1, 2, 3) <= (1, 2, 3))  # True
print((1, 2, 3) == (1, 2, 4))  # False
print((1, 2, 3) != (1, 2, 4))  # True
print((1, 2, 3) > (1, 2, 4))  # False
print((1, 2, 3) < (1, 2, 4))  # True
print((1, 2, 3) >= (1, 2, 4))  # False
print((1, 2, 3) <= (1, 2, 4))  # True

# Comparison Operators with Dictionaries
print("Comparison Operators with Dictionaries")
print({"a": 1, "b": 2} == {"a": 1, "b": 2})  # True
print({"a": 1, "b": 2} != {"a": 1, "b": 2})  # False
print({"a": 1, "b": 2} > {"a": 1, "b": 2})  # False
print({"a": 1, "b": 2} < {"a": 1, "b": 2})  # False
print({"a": 1, "b": 2} >= {"a": 1, "b": 2})  # True
print({"a": 1, "b": 2} <= {"a": 1, "b": 2})  # True
print({"a": 1, "b": 2} == {"a": 1, "b": 3})  # False
print({"a": 1, "b": 2} != {"a": 1, "b": 3})  # True
print({"a": 1, "b": 2} > {"a": 1, "b": 3})  # False
print({"a": 1, "b": 2} < {"a": 1, "b": 3})  # True
print({"a": 1, "b": 2} >= {"a": 1, "b": 3})  # False
print({"a": 1, "b": 2} <= {"a": 1, "b": 3})  # True

# Comparison Operators with Sets
print("Comparison Operators with Sets")
print({1, 2, 3} == {1, 2, 3})  # True
print({1, 2, 3} != {1, 2, 3})  # False
print({1, 2, 3} > {1, 2, 3})  # False
print({1, 2, 3} < {1, 2, 3})  # False
print({1, 2, 3} >= {1, 2, 3})  # True
print({1, 2, 3} <= {1, 2, 3})  # True
print({1, 2, 3} == {1, 2, 4})  # False
print({1, 2, 3} != {1, 2, 4})  # True
print({1, 2, 3} > {1, 2, 4})  # False
print({1, 2, 3} < {1, 2, 4})  # True
print({1, 2, 3} >= {1, 2, 4})  # False
print({1, 2, 3} <= {1, 2, 4})  # True

# Comparison Operators with Booleans
print("Comparison Operators with Booleans")
print(True == True)  # True
print(True != True)  # False
print(True > True)  # False
print(True < True)  # False
print(True >= True)  # True
print(True <= True)  # True
print(True == False)  # False
print(True != False)  # True
print(True > False)  # True
print(True < False)  # False
print(True >= False)  # True
print(True <= False)  # False

# Comparison Operators with None
print("Comparison Operators with None")
print(None == None)  # True
print(None != None)  # False
print(None > None)  # False
print(None < None)  # False
print(None >= None)  # True
print(None <= None)  # True
print(None == 1)  # False
print(None != 1)  # True
print(None > 1)  # False
print(None < 1)  # False
print(None >= 1)  # False
print(None <= 1)  # False

# Comparison Operators with Complex Numbers
print("Comparison Operators with Complex Numbers")
print(1 + 2j == 1 + 2j)  # True
print(1 + 2j != 1 + 2j)  # False
print(1 + 2j > 1 + 2j)  # False
print(1 + 2j < 1 + 2j)  # False
print(1 + 2j >= 1 + 2j)  # True
print(1 + 2j <= 1 + 2j)  # True
print(1 + 2j == 1 + 3j)  # False
print(1 + 2j != 1 + 3j)  # True
print(1 + 2j > 1 + 3j)  # False
print(1 + 2j < 1 + 3j)  # True
print(1 + 2j >= 1 + 3j)  # False
print(1 + 2j <= 1 + 3j)  # True

# Logic Operators
print("Logic Operators")
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print(not True)  # False
print(not False)  # True
print(True and True and True)  # True
print(True and True and False)  # False
print(True and False and True)  # False
print(False and True and True)  # False
print(True or True or True)  # True
print(True or True or False)  # True
print(True or False or True)  # True
print(False or True or True)  # True
print(True or True or False)  # True
print(True or False or False)  # True
print(False or True or True)  # True
print(False or False or True)  # True
print(False or False or False)  # False
print(not True and True)  # False
print(not True and False)  # False
print(not False and True)  # True
print(not False and False)  # False
print(not True or True)  # True
print(not True or False)  # False
print(not False or True)  # True
print(not False or False)  # True
print(not True)  # False
print(not False)  # True
