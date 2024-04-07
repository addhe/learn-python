"""Write a python function that takes a list and returns a new list with unique elements
 of the first list"""

# def unique_list(lst):
#     seen_numbers = []
#     for number in lst:
#         if number not in seen_numbers:
#             seen_numbers.append(number)
#     return seen_numbers


# or we can use this
def unique_list(lst):
    return list(set(lst))


print(
    unique_list([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 7])
)
