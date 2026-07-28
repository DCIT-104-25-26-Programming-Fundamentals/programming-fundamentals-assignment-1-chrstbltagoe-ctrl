# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
)       
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================


def read_matrix(name="Matrix"):
    """Read an M x N matrix from the user, one row at a time."""
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"  Please enter exactly {cols} numbers.")
                continue
            row = [float(x) if '.' in x else int(x) for x in row_input]
            matrix.append(row)
            break

    return matrix, rows, cols


def display_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    if not matrix:
        print("  (empty)")
        return

    # Find the widest element so columns line up
    width = max(len(str(val)) for row in matrix for val in row)
    for row in matrix:
        print("  " + " ".join(str(val).rjust(width) for val in row))


def transpose_matrix(matrix, rows, cols):
    """Return the transpose of matrix (cols x rows)."""
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b, rows, cols):
    """Return element-wise sum of two matrices of the same size."""
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b, m, n, p):
    """Multiply A (m x n) by B (n x p), returning an m x p result."""
    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n" + "=" * 50)
    print("PART A — Transpose a Matrix")
    print("=" * 50)

    matrix, rows, cols = read_matrix("the matrix")
    display_matrix(matrix, "Original Matrix")

    result = transpose_matrix(matrix, rows, cols)
    display_matrix(result, "Transposed Matrix")


def part_b_addition():
    print("\n" + "=" * 50)
    print("PART B — Add Two Matrices")
    print("=" * 50)

    a, rows, cols = read_matrix("Matrix A")
    print(f"\nMatrix B must also be {rows} x {cols}.")
    b, rows_b, cols_b = read_matrix("Matrix B")

    while rows_b != rows or cols_b != cols:
        print("Matrix B must be the same size as Matrix A. Try again.")
        b, rows_b, cols_b = read_matrix("Matrix B")

    display_matrix(a, "Matrix A")
    display_matrix(b, "Matrix B")

    result = add_matrices(a, b, rows, cols)
    display_matrix(result, "Sum (A + B)")


def part_c_multiplication():
    print("\n" + "=" * 50)
    print("PART C — Multiply Two Matrices")
    print("=" * 50)

    a, m, n = read_matrix("Matrix A (M x N)")
    print(f"\nMatrix B must have {n} rows (to match A's columns).")
    b, n_b, p = read_matrix("Matrix B (N x P)")

    while n_b != n:
        print(f"Matrix B must have exactly {n} rows. Try again.")
        b, n_b, p = read_matrix("Matrix B (N x P)")

    display_matrix(a, "Matrix A")
    display_matrix(b, "Matrix B")

    result = multiply_matrices(a, b, m, n, p)
    display_matrix(result, "Product (A x B)")


def main():
    print("MATRIX OPERATIONS PROGRAM")
    part_a_transpose()
    part_b_addition()
    part_c_multiplication()
    print("\nAll operations complete.")


if __name__ == "__main__":
    main()