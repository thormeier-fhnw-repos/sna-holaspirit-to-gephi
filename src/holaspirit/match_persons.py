def match_persons(persons_with_roles, determine_weight):
    """
    Creates a list of pairs of persons that have the same values
    :param persons_with_roles: A dict of persons and roles/circles
    :param determine_weight: A function that determines the weight of the relationship
    :return: List of tuples that contain Person A, Person B and the weight of their relationship
    """

    pairs = []

    for person_a,values_a in persons_with_roles.items():
        for value in values_a:
            for person_b,values_b in persons_with_roles.items():
                # Skip same person
                if person_b == person_a:
                    continue

                if value in values_b:
                    pairs.append((person_a, person_b, determine_weight(value)))

    return pairs
