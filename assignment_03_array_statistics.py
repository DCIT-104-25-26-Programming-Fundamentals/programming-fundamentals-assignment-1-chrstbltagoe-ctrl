# =============================================================================
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
def calculate_sum(numbers):
    """Calculates the total sum of all numbers using a loop."""
    total = 0
    for num in numbers:
        total += num
        return total 

def calculate_average(numbers):
    """Calculates the average of the numbers."""

    if len(numbers) == 0:
        return 0.0

    total = calculate_sum(numbers) 
    return total / len(numbers)  

def find_maximum(numbers):
    """Finds the largest number using a loop."""

    max_val = numbers[0] 
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def find_minimum(numbers):
    """Finds the smallest number using a loop."""

    min_val = numbers[0] 
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def main():

    count = int(input("How many numbers? ")) 

    if count <= 0:
        print("Error: Number of element must be greater than 0.")
        return

    numbers_list = []  
    for i in range(1, count + 1):
        num = float(input(f"Enter number {i}: "))
        numbers_list.append(num) 

    total_sum = calculate_sum(numbers_list)   
    avg = calculate_average(numbers_list) 
    maximum = find_maximum(numbers_list) 
    minimum = find_minimum(numbers_list)  

    print("\nResults:")    
    print(f"Sum:      {total_sum}") 
    print(f"Average:  {avg}")
    print(f"Maximum:  {maximum}") 
    print(f"Minimum:  {minimum}") 

    if __name__ == "__main__":
        main()             
