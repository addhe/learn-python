# Small Project for Python Learning

def main():
    print("Welcome to the Small Project!")
    print("This project applies concepts learned from previous modules.")
    
    # Example of using variables
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's start coding.")

    # Example of a simple function
    def add_numbers(a, b):
        return a + b

    # Get user input for addition
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()