def map_to_list_csv(map, header):
    """
    Creates a CSV-friendly data structure out of a dict
    :param map:
    :return:
    """

    csv_list = list(map.items())
    csv_list.insert(0, header)

    return csv_list