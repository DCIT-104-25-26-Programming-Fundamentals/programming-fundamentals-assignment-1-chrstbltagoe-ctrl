# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: git stat
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci_terms():
    """Part A: Ask the user for N and print the first N Fibonacci terms."""
    n_input = input("How many terms? ")

    # Validate that N is a positive integer
    if not n_input.isdigit() or int(n_input) <= 0:
        print("Error: N must be a positive integer.")
        return

    n = int(n_input)

    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    # Convert numbers to strings so they can be joined with spaces
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def check_fibonacci_number():
    """Part B: Ask the user for a number and check if it's a Fibonacci number."""
    num_input = input("Enter a number to check: ")

    if not num_input.isdigit():
        print("Error: please enter a valid non-negative integer.")
        return

    num = int(num_input)

    # Generate Fibonacci numbers with a loop until we reach or pass num
    a, b = 0, 1
    is_fibonacci = False
    while a <= num:
        if a == num:
            is_fibonacci = True
            break
        a, b = b, a + b

    if is_fibonacci:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


def main():
    print_fibonacci_terms()
    print()  # blank line for readability
    check_fibonacci_number()


if __name__ == "__main__":
    main()