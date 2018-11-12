import csv

def read_csv(filename):
    """
    Reads contents of a given file
    :param filename:
    :return: CSV data
    """
    with (open(filename, "r")) as csvfile:
        rows = []
        csv_reader = csv.reader(csvfile, delimiter=",", quotechar="\"")
        for row in csv_reader:
            rows.append(row)

    return rows
