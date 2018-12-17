def create_empty_matrix(distinct_persons):
    """
    Creates an empty matrix (all 0) for a given list of distinct persons
    :param distinct_persons: List of distinct persons
    :return: EMpty matrix
    """
    no_persons = len(distinct_persons) + 1  # Header/left-most col containing names

    # Prepare matrix full of 0s, we only need to fill in 1s
    matrix = [[0 for _ in range(no_persons)] for _ in range(no_persons)]

    matrix[0][0] = ""

    for i in range(1, no_persons):
        matrix[0][i] = distinct_persons[i - 1]
        matrix[i][0] = distinct_persons[i - 1]

    return matrix