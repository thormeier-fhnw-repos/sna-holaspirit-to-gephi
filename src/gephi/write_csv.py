import csv

def write_csv(matrix, file_name):
    """
    Writes a given matrix into a CSV file
    :param matrix: The matrix to write
    :return: None
    """
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(matrix)
