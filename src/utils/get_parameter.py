import sys

def get_parameter(name):
    """
    Retrieves an argumen from CLI
    :param name: Name of the argument to retrieve
    :return: The value of the argument or None
    """
    key = "--" + name + "="
    for arg in sys.argv:
        if key in arg:
            return arg.replace(key, "")

    return None
