# This file contains exercises and examples related to dictionaries.

def create_dictionary():
    # Create a sample dictionary
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    return sample_dict

def print_dictionary_info(dictionary):
    # Print the keys and values of the dictionary
    for key, value in dictionary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    my_dict = create_dictionary()
    print_dictionary_info(my_dict)