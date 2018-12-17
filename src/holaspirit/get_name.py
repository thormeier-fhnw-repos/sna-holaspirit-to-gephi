def get_name(row):
    """
    Returns a built string containing of last name and first name
    :param row: Raw row from CSV
    :return: Name string
    """
    return row[0] + " " + row[1]