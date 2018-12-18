def map_to_list_csv(map, header):
    """
    Creates a CSV-friendly data structure out of a dict
    :param map:
    :return:
    """

    csv_list = list(map.items())

    csv_list = [list(item) for item in csv_list]

    flattend_csv_list = list()
    for sub_list in csv_list:
        if type(sub_list[1]) is list:
            sub_list[1].insert(0, sub_list[0])
            flattend_csv_list.append(sub_list[1])
        else:
            flattend_csv_list.append(sub_list)

    flattend_csv_list.insert(0, header)

    return flattend_csv_list