def anonymize(person_names, should_anonymize):
    """
    Creates a map of person names.
    :param person_names: List of person names
    :param should_anonymize: If person names should be anonymized
    :return:
    """

    person_name_dict = dict()

    person_counter = 1

    for person_name in person_names:
        person_name_dict[person_name] = ("Person #" + str(person_counter)) if should_anonymize else person_name
        person_counter += 1

    return person_name_dict
