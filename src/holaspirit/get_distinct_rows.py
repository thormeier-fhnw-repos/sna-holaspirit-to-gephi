def get_distinct_rows(data_raw, processor, filter):
    """
    Gets distinct rows out of raw data. Can be used for statistics
    :param data_raw: The raw CSV data
    :param processor: How to process a given row
    :param filter: Filter that determines if the row should be added or not
    :return:
    """
    rows  = []

    has_handled_header = False

    for row in data_raw:
        if has_handled_header == False:
            has_handled_header = True
            continue

        value = processor(row)

        if filter(value):
            rows.append(value)

    return list(set(rows))
