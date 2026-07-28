# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
# =============================================================================


def print_single_table():
    """Part A: Ask the user for a number and print its multiplication table (1-12)."""
    num_input = input("Enter a number: ")

    if not num_input.lstrip("-").isdigit():
        print("Error: please enter a valid integer.")
        return

    num = int(num_input)

    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        # Using formatted alignment so the output lines up neatly
        print(f"{num:<3}x{i:>3} = {num * i}")


def print_tables_up_to_n():
    """Part B: Ask the user for N and print multiplication tables from 1 to N."""
    n_input = input("Enter a number N: ")

    if not n_input.isdigit() or int(n_input) <= 0:
        print("Error: N must be a positive integer.")
        return

    n = int(n_input)

    for table_num in range(1, n + 1):
        print(f"Multiplication Table for {table_num}:")
        for i in range(1, 13):
            print(f"{table_num:<3}x{i:>3} = {table_num * i}")

        # Separator between tables (skip after the very last one)
        if table_num != n:
            print("-" * 29)


def main():
    print_single_table()
    print()
    print_tables_up_to_n()


if __name__ == "__main__":
    main()
