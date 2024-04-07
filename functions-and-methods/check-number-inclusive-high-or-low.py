# Write a function that checks whether a number is in given range ( inclusive of high and low )
def ran_check(num, low, high):
    if num in range(low, high + 1):
        print(f"{num} is in range of low and high")
    else:
        print("not in range of low and high")


ran_check(10, 4, 14)
