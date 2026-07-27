=====================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# def get_numbers():
    """Prompt the user for how many numbers to enter, then collect them."""
    count = int(input("How many numbers? "))

    numbers = []
    for i in range(1, count + 1):
        value = float(input(f"Enter number {i}: "))
        numbers.append(value)

    return numbers


def calculate_sum(numbers):
    """Return the sum of all numbers in the list."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of all numbers in the list."""
    return calculate_sum(numbers) / len(numbers)


def calculate_max(numbers):
    """Return the largest number in the list."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def calculate_min(numbers):
    """Return the smallest number in the list."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    numbers = get_numbers()

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_max(numbers)
    minimum = calculate_min(numbers)

    # Format numbers cleanly: show as int if they're whole numbers
    def fmt(n):
        return int(n) if n == int(n) else n

    print("\nResults:")
    print(f"Sum:     {fmt(total)}")
    print(f"Average: {round(average, 2)}")
    print(f"Maximum: {fmt(maximum)}")
    print(f"Minimum: {fmt(minimum)}")


if __name__ == "__main__":
    main()========