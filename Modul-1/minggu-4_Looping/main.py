# This file contains examples of looping in Python.

def while_loop_example():
    print("While Loop Example:")
    count = 0
    while count < 5:
        print("Count is:", count)
        count += 1

def for_loop_example():
    print("\nFor Loop Example:")
    for i in range(5):
        print("Iteration:", i)

if __name__ == "__main__":
    while_loop_example()
    for_loop_example()