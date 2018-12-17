from src.gephi.create_empty_matrix import create_empty_matrix

def build_matrix(distinct_persons, pairs):
    """
    Creates a NxN matrix that represents which individual of a list of piars is matched with whom
    Should be importable in Gephi
    :param distinct_persons: A list of distinct person names
    :param pairs: A list of pairs and their weight
    :param anonymize: If the list should be anonymized, i.e. replacing names with numbers
    :return: Matrix that has all connections as 1, missing connections as 0
    """

    matrix = create_empty_matrix(distinct_persons)

    for pair in pairs:
        x = distinct_persons.index(pair[0]) + 1
        y = distinct_persons.index(pair[1]) + 1

        if x == y:
            continue

        matrix[x][y] += pair[2]

    return matrix