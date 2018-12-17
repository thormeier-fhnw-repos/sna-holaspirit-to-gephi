def list_to_dict(l):
    """
    COnverts a list to a dict
    :param l:
    :return:
    """
    res = dict()

    for row in l:
        res[row[0]] = row[1:]

    return res