#def read_matrix(name="matrix"):
    """Read an M x N matrix from the user, one row per line."""
    print(f"\n--- Enter {name} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for i in range(1, rows + 1):
        row_input = input(f"Enter row {i}: ")
        row = [float(x) for x in row_input.split()]

        # Basic safety check: make sure the row has the right number of values
        while len(row) != cols:
            print(f"Expected {cols} values, got {len(row)}. Try again.")
            row_input = input(f"Enter row {i}: ")
            row = [float(x) for x in row_input.split()]

        matrix.append(row)

    return matrix


def display_matrix(matrix):
    """Print a matrix in a readable grid format."""
    for row in matrix:
        print("  ".join(fmt(val) for val in row))


def fmt(n):
    """Format a number as an int if it's a whole number, else as-is."""
    return str(int(n)) if n == int(n) else str(n)


def transpose_matrix(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)

    return result


def add_matrices(a, b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(a)
    cols = len(a[0])

    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(a[r][c] + b[r][c])
        result.append(new_row)

    return result


def multiply_matrices(a, b):
    """Return the matrix product A x B, where A is MxN and B is NxP."""
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    # Result is rows_a x cols_b, every cell starts at 0
    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n=== PART A: Transpose a Matrix ===")
    matrix = read_matrix("matrix")

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    result = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(result)


def part_b_add():
    print("\n=== PART B: Add Two Matrices ===")
    print("Matrix A and Matrix B must be the same size (M x N).")

    matrix_a = read_matrix("Matrix A")
    matrix_b = read_matrix("Matrix B")

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Error: Matrices must be the same size to add them.")
        return

    result = add_matrices(matrix_a, matrix_b)

    print("\nSum of Matrices:")
    display_matrix(result)


def part_c_multiply():
    print("\n=== PART C: Multiply Two Matrices ===")
    print("Matrix A (M x N) and Matrix B (N x P) — columns of A must match rows of B.")

    matrix_a = read_matrix("Matrix A")
    matrix_b = read_matrix("Matrix B")

    if len(matrix_a[0]) != len(matrix_b):
        print("Error: Number of columns in A must equal number of rows in B.")
        return

    result = multiply_matrices(matrix_a, matrix_b)

    print("\nProduct of Matrices (A x B):")
    display_matrix(result)


def main():
    print("Matrix Operations Program")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    print("4. Run All")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_add()
    elif choice == "3":
        part_c_multiply()
    elif choice == "4":
        part_a_transpose()
        part_b_add()
        part_c_multiply()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main( =============================================================================
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

