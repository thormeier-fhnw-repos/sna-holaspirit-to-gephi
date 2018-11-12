from pprint import pprint

def build_matrix(distinct_persons, pairs, anonymize):
    """
    Creates a NxN matrix that represents which individual of a list of piars is matched with whom
    Should be importable in Gephi
    :param distinct_persons: A list of distinct person names
    :param pairs: A list of pairs and their weight
    :param anonymize: If the list should be anonymized, i.e. replacing names with numbers
    :return: Matrix that has all connections as 1, missing connections as 0
    """

    no_persons = len(distinct_persons) + 1 # Header/left-most col containing names

    # Prepare matrix full of 0s, we only need to fill in 1s
    matrix = [[0 for col in range(no_persons)] for row in range(no_persons)]

    matrix[0][0] = ""

    for pair in pairs:
        x = distinct_persons.index(pair[0]) + 1
        y = distinct_persons.index(pair[1]) + 1

        matrix[x][0] = pair[0] if not anonymize else distinct_persons.index(pair[0])
        matrix[0][y] = pair[1] if not anonymize else distinct_persons.index(pair[1])
        matrix[x][y] = pair[2]

    return matrix