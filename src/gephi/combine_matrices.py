from src.gephi.create_empty_matrix import create_empty_matrix

def combine_matrices(a, b, distinct_persons):
    """
    Combines two matrices a und b
    :param a: Matrix A
    :param b: Matrix B
    :param distinct_persons: Distinct persons of the new matrix
    :return:
    """

    matrix = create_empty_matrix(distinct_persons)

    for x in range(1, len(a)):
        for y in range(1, len(a)):
            matrix[x][y] = a[x][y] + b[x][y]

    return matrix
