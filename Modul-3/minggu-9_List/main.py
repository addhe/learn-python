# This file contains exercises and examples related to lists in Python.

def main():
    # Example of creating a list
    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)

    # Example of adding an element to the list
    my_list.append(6)
    print("List after appending 6:", my_list)

    # Example of removing an element from the list
    my_list.remove(3)
    print("List after removing 3:", my_list)

    # Example of accessing elements in the list
    print("First element:", my_list[0])
    print("Last element:", my_list[-1])

    # Example of iterating through the list
    print("Iterating through the list:")
    for item in my_list:
        print(item)

if __name__ == "__main__":
    main()