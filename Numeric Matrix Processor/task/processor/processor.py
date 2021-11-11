import matrices


ADD_MATRICES_OPTION = "1"
MULTIPLY_MATRIX_BY_CONSTANT_OPTION = "2"
MULTIPLY_MATRICES_OPTION = "3"
TRANSPOSE_MATRIX_OPTION = "4"
CALCULATE_DETERMINANT_OPTION = "5"
FIND_INVERSE_OPTION = "6"
EXIT_OPTION = "0"


TRANSPOSITION_MAIN_DIAGONAL = "1"
TRANSPOSITION_SIDE_DIAGONAL = "2"
TRANSPOSITION_VERTICAL_LINE = "3"
TRANSPOSITION_HORIZONTAL_LINE = "4"


def perform_action(option):
    if option == ADD_MATRICES_OPTION:
        add_matrices()
    elif option == MULTIPLY_MATRIX_BY_CONSTANT_OPTION:
        multiply_matrix_by_constant()
    elif option == MULTIPLY_MATRICES_OPTION:
        multiply_matrices()
    elif option == TRANSPOSE_MATRIX_OPTION:
        transpose_matrix()
    elif option == CALCULATE_DETERMINANT_OPTION:
        calculate_determinant()
    elif option == FIND_INVERSE_OPTION:
        find_inverse()
    elif option != EXIT_OPTION:
        print("Wrong option")


def add_matrices():
    num_rows_a, num_cols_a = matrices.read_matrix_dimensions("Enter size of first matrix: ")
    matrix_a = matrices.read_matrix(num_rows_a, num_cols_a, "Enter first matrix:")
    num_rows_b, num_cols_b = matrices.read_matrix_dimensions("Enter size of second matrix: ")
    matrix_b = matrices.read_matrix(num_rows_b, num_cols_b, "Enter second matrix:")
    if num_rows_a != num_rows_b or num_cols_a != num_cols_b:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        result = matrices.add_matrices(matrix_a, matrix_b)
        matrices.print_matrix(result)


def multiply_matrix_by_constant():
    num_rows, num_cols = matrices.read_matrix_dimensions("Enter size of matrix: ")
    matrix = matrices.read_matrix(num_rows, num_cols, "Enter matrix:")
    constant = float(input("Enter constant: "))
    result = matrices.multiply_matrix_by_constant(matrix, constant)
    print("The result is:")
    matrices.print_matrix(result)


def multiply_matrices():
    num_rows_a, num_cols_a = matrices.read_matrix_dimensions("Enter size of first matrix: ")
    matrix_a = matrices.read_matrix(num_rows_a, num_cols_a, "Enter first matrix:")
    num_rows_b, num_cols_b = matrices.read_matrix_dimensions("Enter size of second matrix: ")
    matrix_b = matrices.read_matrix(num_rows_b, num_cols_b, "Enter second matrix:")
    if num_cols_a != num_rows_b:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        result = matrices.multiply_matrices(matrix_a, matrix_b)
        matrices.print_matrix(result)


def transpose_matrix():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    transposition_option = input("Your choice: ")
    num_rows, num_cols = matrices.read_matrix_dimensions("Enter matrix size: ")
    matrix = matrices.read_matrix(num_rows, num_cols, "Enter matrix:")
    result = perform_transposition(transposition_option, matrix)
    print("The result is:")
    matrices.print_matrix(result)


def perform_transposition(transposition_option, matrix):
    if transposition_option == TRANSPOSITION_MAIN_DIAGONAL:
        return matrices.transpose_by_main_diagonal(matrix)
    elif transposition_option == TRANSPOSITION_SIDE_DIAGONAL:
        return matrices.transpose_by_side_diagonal(matrix)
    elif transposition_option == TRANSPOSITION_VERTICAL_LINE:
        return matrices.transpose_by_vertical_line(matrix)
    elif transposition_option == TRANSPOSITION_HORIZONTAL_LINE:
        return matrices.transpose_by_horizontal_line(matrix)
    else:
        print("Wrong option")


def calculate_determinant():
    num_rows, num_cols = matrices.read_matrix_dimensions("Enter matrix size: ")
    matrix = matrices.read_matrix(num_rows, num_cols, "Enter matrix:")
    if matrix.num_rows != matrix.num_cols or matrix.num_rows < 0:
        print("The operation cannot be performed.")
    else:
        result = matrices.calculate_determinant(matrix)
        print("The result is:")
        print(result)


def find_inverse():
    num_rows, num_cols = matrices.read_matrix_dimensions("Enter matrix size: ")
    matrix = matrices.read_matrix(num_rows, num_cols, "Enter matrix:")
    if matrix.num_rows != matrix.num_cols or matrix.num_rows < 0:
        print("The operation cannot be performed.")
    else:
        result = matrices.inverse(matrix)
        if result:
            print("The result is:")
            matrices.print_matrix(result, use_rounding=True)
        else:
            print("This matrix doesn't have an inverse.")


def main():
    option = ""
    while option != EXIT_OPTION:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
        option = input("Your choice: ")
        perform_action(option)
        print()


if __name__ == "__main__":
    main()
