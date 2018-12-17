from src.holaspirit.get_role import get_role

def get_circle(row):
    """
    Extracts the circle from a given row
    :param row: The row to look at
    :return: The circle with its given weight (lead link, rep link are + 0.5)
    """
    role_in_circle = get_role(row)

    weight = 1.5 if role_in_circle == "Lead Link" or role_in_circle == "Rep Link" else 1

    return (row[5], weight)
