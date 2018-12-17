def get_person_dict(data_raw, name_map, get_value):
    """
    Creates a dict with a persons name as key and all their "values" as a list as value
    :param data_raw: Raw data
    :param name_map: Maps names to either names or anonymized names
    :param get_value: Function to receive a value from a given row
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

        if not name_map[name] in list(persons):
            persons[name_map[name]] = []

        persons[name_map[name]].append(get_value(row))

    return persons
