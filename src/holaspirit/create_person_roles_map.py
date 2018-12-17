from src.holaspirit.get_role import get_role
from src.holaspirit.get_name import get_name

def create_person_roles_map(person_rows):
    """
    Creates a dict of names and all of their roles, separated by ;
    :param person_rows: Raw roles of the export CSV
    :return: The map
    """
    person_roles_map = dict()

    has_handled_header = False

    for row in person_rows:
        if not has_handled_header:
            has_handled_header = True
            continue

        name = get_name(row)
        role = get_role(row)

        if name == " ": # Ignore empty name
            continue

        if not name in person_roles_map:
            person_roles_map[name] = []

        if not role in person_roles_map[name]:
            person_roles_map[name].append(role)

    person_roles_map = {k: ";".join(v) for k, v in person_roles_map.items()}

    return person_roles_map