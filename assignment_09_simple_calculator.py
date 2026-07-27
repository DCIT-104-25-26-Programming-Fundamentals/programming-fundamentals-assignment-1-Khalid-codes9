# def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    """Return the remainder of a divided by b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def exponent(a, b):
    """Return a raised to the power of b."""
    return a ** b


def fmt(n):
    """Format a number as an int if it's a whole number, else round to 2dp."""
    if n == int(n):
        return str(int(n))
    return str(round(n, 2))


def get_numbers():
    """Prompt for two numbers and return them as floats."""
    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))
    return first, second


def perform_operation(choice):
    """Run the operation matching the menu choice and print the result."""
    first, second = get_numbers()

    if choice == "1":
        result = add(first, second)
        symbol = "+"
    elif choice == "2":
        result = subtract(first, second)
        symbol = "-"
    elif choice == "3":
        result = multiply(first, second)
        symbol = "*"
    elif choice == "4":
        result = divide(first, second)
        symbol = "/"
    elif choice == "5":
        result = modulus(first, second)
        symbol = "%"
    elif choice == "6":
        result = exponent(first, second)
        symbol = "**"

    if result is None:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {fmt(first)} {symbol} {fmt(second)} = {fmt(result)}")


def print_menu():
    """Display the menu options."""
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice in ("1", "2", "3", "4", "5", "6"):
            perform_operation(choice)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()=============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

