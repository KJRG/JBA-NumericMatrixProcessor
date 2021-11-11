from number_formatting import format_number


class Matrix:
    def __init__(self, num_rows, num_cols, elements):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.elements = elements


def read_matrix_dimensions(prompt):
    dimensions = input(prompt).split()
    return int(dimensions[0]), int(dimensions[1])


def read_matrix(num_rows, num_cols, prompt):
    print(prompt)
    rows = list()
    for i in range(num_rows):
        row_elements = [float(x) for x in input().split()]
        rows.append(row_elements)
    return Matrix(num_rows, num_cols, rows)


def print_matrix(matrix, use_rounding=False):
    format_function = format_number if use_rounding else str
    for row in matrix.elements:
        row_elements_str = " ".join(map(format_function, row))
        print(row_elements_str)


def add_matrices(m_a, m_b):
    result_elements = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(m_a.elements, m_b.elements)]
    return Matrix(m_a.num_rows, m_a.num_cols, result_elements)


def multiply_matrix_by_constant(matrix, constant):
    result_elements = [[x * constant for x in row] for row in matrix.elements]
    return Matrix(matrix.num_rows, matrix.num_cols, result_elements)


def multiply_matrices(a, b):
    result_rows = list()
    for i in range(a.num_rows):
        result_row = list()
        for j in range(b.num_cols):
            row_a = a.elements[i]
            col_b = [r[j] for r in b.elements]
            element = dot_product(row_a, col_b)
            result_row.append(element)
        result_rows.append(result_row)
    return Matrix(a.num_rows, b.num_cols, result_rows)


def dot_product(v_1, v_2):
    return sum([e_1 * e_2 for e_1, e_2 in zip(v_1, v_2)])


def transpose_by_main_diagonal(matrix):
    rows = matrix.elements
    result_rows = [[col[i] for col in rows] for i in range(matrix.num_cols)]
    return Matrix(matrix.num_cols, matrix.num_rows, result_rows)


def transpose_by_side_diagonal(matrix):
    rows = matrix.elements
    result_rows = [[col[i] for col in rows[::-1]] for i in reversed(range(matrix.num_cols))]
    return Matrix(matrix.num_cols, matrix.num_rows, result_rows)


def transpose_by_vertical_line(matrix):
    rows = matrix.elements
    result_rows = [r[::-1] for r in rows]
    return Matrix(matrix.num_rows, matrix.num_cols, result_rows)


def transpose_by_horizontal_line(matrix):
    rows = matrix.elements
    result_rows = [r for r in rows[::-1]]
    return Matrix(matrix.num_rows, matrix.num_cols, result_rows)


def calculate_determinant(matrix):
    size = matrix.num_rows

    if size < 1:
        return None

    if size == 1:
        return matrix.elements[0][0]

    if size == 2:
        return matrix.elements[0][0] * matrix.elements[1][1] - matrix.elements[1][0] * matrix.elements[0][1]

    det = 0.0
    for j in range(matrix.num_cols):
        det += matrix.elements[0][j] * cofactor(matrix, 0, j)
    return det


def cofactor(matrix, i, j):
    cofactor_sign = (-1) ** (i + j)
    minor_matrix = remove_row_and_column(matrix, i, j)
    return cofactor_sign * calculate_determinant(minor_matrix)


def remove_row_and_column(matrix, row_num, col_num):
    minor_matrix_elements = list()
    for i in range(matrix.num_rows):
        if i == row_num:
            continue
        minor_matrix_row = list()
        for j in range(matrix.num_cols):
            if j == col_num:
                continue
            minor_matrix_row.append(matrix.elements[i][j])
        minor_matrix_elements.append(minor_matrix_row)

    return Matrix(matrix.num_rows - 1, matrix.num_cols - 1, minor_matrix_elements)


def inverse(matrix):
    det = calculate_determinant(matrix)
    if not det:
        return None
    return multiply_matrix_by_constant(adjoint(matrix), 1 / det)


def adjoint(matrix):
    cofactor_matrix_elements = list()
    for i in range(matrix.num_rows):
        cofactor_matrix_row = list()
        for j in range(matrix.num_cols):
            cofactor_matrix_row.append(cofactor(matrix, i, j))
        cofactor_matrix_elements.append(cofactor_matrix_row)
    cofactor_matrix = Matrix(matrix.num_rows, matrix.num_cols, cofactor_matrix_elements)
    return transpose_by_main_diagonal(cofactor_matrix)
