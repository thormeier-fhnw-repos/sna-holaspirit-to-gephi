def get_role(row):
    """
    Extracts the role from a given row
    :param row: Row to look at
    :return: The role
    """
    role = row[6]

    # Normalize roles Lead Link and Rep Link, as they contain the circle name as well
    if "Lead Link" in role:
        role = "Lead Link"

    if "Rep Link" in role:
        role = "Rep Link"

    return role
