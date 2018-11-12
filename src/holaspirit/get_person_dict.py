def get_person_dict(data_raw, get_value):
    """
    Creates a dict with a persons name as key and all their "values" as a list as value
    :param data_raw: Raw data
    :return: Persons with their roles
    """
    persons = dict()

    has_handled_header = False

    for row in data_raw:
        if has_handled_header == False:
            has_handled_header = True
            continue

        name = row[0] + " " + row[1]
        # Skip empty rows
        if len(name) <= 1:
            continue

        if not name in list(persons):
            persons[name] = []

        persons[name].append(get_value(row))

    return persons
